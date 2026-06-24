"""
crawler.py
----------
A simple, polite, breadth-first web crawler.

What it does:
1. Starts from SEED_URLS in config.py
2. Downloads each page
3. Extracts the page title + visible text
4. Extracts internal links to crawl next
5. Saves everything into a SQLite database (pages.db)

Run it directly:
    python crawler.py
"""

import sqlite3
import time
from collections import deque
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

import config


def create_database():
    """
    Creates the SQLite database and the 'pages' table if they don't exist.
    Each row = one crawled page.
    """
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE NOT NULL,
            title TEXT,
            content TEXT,
            crawled_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn


def is_allowed(url: str) -> bool:
    """
    Decide whether a discovered link should be crawled.
    Currently: must belong to ALLOWED_DOMAIN and not be a file
    (pdf/jpg/etc) or a non-http(s) link (mailto:, javascript:, etc.)
    """
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        return False

    if config.ALLOWED_DOMAIN not in parsed.netloc:
        return False

    # Skip common non-HTML file types
    blocked_extensions = (".pdf", ".jpg", ".jpeg", ".png", ".gif", ".zip", ".svg")
    if parsed.path.lower().endswith(blocked_extensions):
        return False

    return True


def normalize_url(url: str) -> str:
    """
    Strip URL fragments (#section) so we don't treat
    'page#intro' and 'page#history' as different pages.
    """
    parsed = urlparse(url)
    return parsed._replace(fragment="").geturl()


def extract_page(url: str, html: str):
    """
    Given raw HTML, extract:
      - a clean title
      - clean visible text (no scripts/styles/nav clutter)
      - a list of internal links found on the page

    Returns (title, text, links)
    """
    soup = BeautifulSoup(html, "html.parser")

    # --- Title ---
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else url

    # --- Remove tags that aren't real page content ---
    for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
        tag.decompose()

    # --- Extract visible text ---
    raw_text = soup.get_text(separator=" ")
    # Collapse multiple spaces/newlines into single spaces
    text = " ".join(raw_text.split())

    # --- Extract links ---
    links = []
    for a_tag in soup.find_all("a", href=True):
        absolute_url = urljoin(url, a_tag["href"])
        absolute_url = normalize_url(absolute_url)
        if is_allowed(absolute_url):
            links.append(absolute_url)

    return title, text, links


def save_page(conn, url, title, content):
    """
    Insert or update a page in the database.
    Uses INSERT OR REPLACE so re-running the crawler refreshes content.
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pages (url, title, content)
        VALUES (?, ?, ?)
        ON CONFLICT(url) DO UPDATE SET
            title = excluded.title,
            content = excluded.content,
            crawled_at = CURRENT_TIMESTAMP
    """, (url, title, content))
    conn.commit()


def crawl():
    """
    Main crawl loop: breadth-first traversal starting from SEED_URLS,
    respecting MAX_PAGES and MAX_DEPTH.
    """
    conn = create_database()

    visited = set()
    # Each queue item is (url, depth)
    queue = deque((url, 0) for url in config.SEED_URLS)

    pages_crawled = 0

    print(f"🚀 Starting crawl. Max pages: {config.MAX_PAGES}, Max depth: {config.MAX_DEPTH}")

    while queue and pages_crawled < config.MAX_PAGES:
        url, depth = queue.popleft()
        url = normalize_url(url)

        if url in visited:
            continue
        visited.add(url)

        try:
            print(f"  [{pages_crawled + 1}/{config.MAX_PAGES}] Crawling (depth {depth}): {url}")
            response = requests.get(url, headers=config.HEADERS, timeout=10)
            response.raise_for_status()

            # Skip non-HTML responses (e.g. PDFs that slipped through)
            content_type = response.headers.get("Content-Type", "")
            if "text/html" not in content_type:
                continue

            title, text, links = extract_page(url, response.text)

            # Skip pages with almost no content
            if len(text) < 100:
                continue

            save_page(conn, url, title, text)
            pages_crawled += 1

            # Queue up new links if we haven't hit max depth
            if depth < config.MAX_DEPTH:
                for link in links:
                    if link not in visited:
                        queue.append((link, depth + 1))

            time.sleep(config.CRAWL_DELAY_SECONDS)

        except requests.RequestException as e:
            print(f"  ⚠️  Failed to fetch {url}: {e}")
            continue

    conn.close()
    print(f"✅ Crawl complete. {pages_crawled} pages saved to {config.DB_PATH}")


if __name__ == "__main__":
    crawl()
