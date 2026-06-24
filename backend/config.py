"""
config.py
---------
Central place for all settings. Change seed URLs, crawl depth,
and file paths here without touching the rest of the code.
"""

import os

# Folder where this config.py lives (backend/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Make sure the data folder exists
os.makedirs(DATA_DIR, exist_ok=True)

# Where we store raw crawled pages
DB_PATH = os.path.join(DATA_DIR, "pages.db")

# Where we store the search index (inverted index + BM25 stats)
INDEX_PATH = os.path.join(DATA_DIR, "index.json")

# --- Crawler settings ---

# Seed URLs: where the crawler starts.
# Add/remove URLs here to change what gets indexed.
SEED_URLS = [
    "https://en.wikipedia.org/wiki/Search_engine",
    "https://en.wikipedia.org/wiki/Web_crawler",
    "https://en.wikipedia.org/wiki/Information_retrieval",
]

# Only crawl links that contain this domain (keeps the crawler "on topic"
# and prevents it from wandering off to random external sites)
ALLOWED_DOMAIN = "en.wikipedia.org"

# Max number of pages to crawl in one run (safety limit so you don't
# accidentally crawl thousands of pages on your first try)
MAX_PAGES = 40

# Max link "depth" from a seed URL (0 = only seed pages, 1 = seed + their
# direct links, etc.)
MAX_DEPTH = 1

# Be polite: wait this many seconds between requests to the same site
CRAWL_DELAY_SECONDS = 1.0

# Some sites block requests with no User-Agent header
HEADERS = {
    "User-Agent": "MiniSearchEngineBot/1.0 (+https://github.com/yourname/mini-search-engine)"
}
