"""
indexer.py
----------
Builds an inverted index from the pages stored in SQLite, and
pre-computes the statistics needed for BM25 ranking at search time.

An "inverted index" maps: word -> list of (page_id, term_frequency)
This is the data structure that makes search fast — instead of scanning
every document for every query, we look up the query words directly.

Run it directly (after crawler.py):
    python indexer.py
"""

import json
import re
import sqlite3
from collections import Counter, defaultdict

import config

# A small list of common English words that don't help distinguish
# documents ("stopwords"). Removing them shrinks the index and improves
# ranking quality.
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "is", "are", "was", "were", "be",
    "been", "being", "in", "on", "at", "to", "for", "of", "with", "by",
    "from", "as", "this", "that", "these", "those", "it", "its", "into",
    "than", "then", "so", "such", "not", "no", "do", "does", "did", "can",
    "could", "will", "would", "should", "has", "have", "had", "i", "you",
    "he", "she", "we", "they", "their", "his", "her", "our", "your"
}

TOKEN_PATTERN = re.compile(r"[a-zA-Z0-9]+")


def tokenize(text: str):
    """
    Convert raw text into a clean list of lowercase word tokens,
    with stopwords removed.

    Example: "The Cat Sat!" -> ["cat", "sat"]
    """
    words = TOKEN_PATTERN.findall(text.lower())
    return [w for w in words if w not in STOPWORDS and len(w) > 1]


def load_pages_from_db():
    """Read all crawled pages from SQLite."""
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, url, title, content FROM pages")
    rows = cursor.fetchall()
    conn.close()
    return rows


def build_index():
    """
    Builds and saves the search index as a JSON file with this shape:

    {
      "documents": {
          "1": {"url": "...", "title": "...", "length": 532},
          ...
      },
      "inverted_index": {
          "python": {"1": 4, "7": 2},   # doc_id -> term frequency
          "search": {"1": 2, "3": 5},
          ...
      },
      "avg_doc_length": 410.5,
      "total_docs": 40
    }
    """
    rows = load_pages_from_db()

    if not rows:
        print("⚠️  No pages found in database. Run crawler.py first.")
        return

    documents = {}
    inverted_index = defaultdict(dict)
    total_length = 0

    for doc_id, url, title, content in rows:
        tokens = tokenize(content)
        term_counts = Counter(tokens)

        documents[str(doc_id)] = {
            "url": url,
            "title": title,
            # Store a short preview/snippet for showing in results later
            "snippet": content[:300],
            "length": len(tokens),
        }
        total_length += len(tokens)

        for term, freq in term_counts.items():
            inverted_index[term][str(doc_id)] = freq

    avg_doc_length = total_length / len(documents) if documents else 0

    index_data = {
        "documents": documents,
        "inverted_index": inverted_index,
        "avg_doc_length": avg_doc_length,
        "total_docs": len(documents),
    }

    with open(config.INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index_data, f)

    print(f"✅ Index built: {len(documents)} documents, "
          f"{len(inverted_index)} unique terms.")
    print(f"   Saved to {config.INDEX_PATH}")


if __name__ == "__main__":
    build_index()
