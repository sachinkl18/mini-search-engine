"""
config.py
---------
Central settings. Add more seed URLs here to expand what gets indexed.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, "pages.db")
INDEX_PATH = os.path.join(DATA_DIR, "index.json")

# ---------------------------------------------------------------
# SEED URLS — these are the starting pages the crawler visits.
# The crawler also follows links FROM these pages (depth=1),
# so each seed URL brings in ~10-20 more pages automatically.
# ---------------------------------------------------------------
SEED_URLS = [
    # Technology & Internet companies
    "https://en.wikipedia.org/wiki/Google",
    "https://en.wikipedia.org/wiki/Amazon_(company)",
    "https://en.wikipedia.org/wiki/Flipkart",
    "https://en.wikipedia.org/wiki/Facebook",
    "https://en.wikipedia.org/wiki/Apple_Inc.",
    "https://en.wikipedia.org/wiki/Microsoft",
    "https://en.wikipedia.org/wiki/Netflix",
    "https://en.wikipedia.org/wiki/Twitter",
    "https://en.wikipedia.org/wiki/Instagram",
    "https://en.wikipedia.org/wiki/YouTube",
    "https://en.wikipedia.org/wiki/WhatsApp",
    "https://en.wikipedia.org/wiki/Uber",
    "https://en.wikipedia.org/wiki/Tesla,_Inc.",

    # India-specific
    "https://en.wikipedia.org/wiki/India",
    "https://en.wikipedia.org/wiki/Bangalore",
    "https://en.wikipedia.org/wiki/Mumbai",
    "https://en.wikipedia.org/wiki/Tata_Group",
    "https://en.wikipedia.org/wiki/Infosys",
    "https://en.wikipedia.org/wiki/Reliance_Industries",
    "https://en.wikipedia.org/wiki/ISRO",

    # Science & Technology
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Python_(programming_language)",
    "https://en.wikipedia.org/wiki/JavaScript",
    "https://en.wikipedia.org/wiki/Smartphone",
    "https://en.wikipedia.org/wiki/Internet",
    "https://en.wikipedia.org/wiki/Cryptocurrency",
    "https://en.wikipedia.org/wiki/Bitcoin",

    # General knowledge
    "https://en.wikipedia.org/wiki/World_War_II",
    "https://en.wikipedia.org/wiki/Climate_change",
    "https://en.wikipedia.org/wiki/Football",
    "https://en.wikipedia.org/wiki/Cricket",
    "https://en.wikipedia.org/wiki/Elon_Musk",
    "https://en.wikipedia.org/wiki/Narendra_Modi",
]

ALLOWED_DOMAIN = "en.wikipedia.org"

# Increase this to crawl more pages (more = better search results)
MAX_PAGES = 150

# Depth 1 = seed pages + all links found on those pages
MAX_DEPTH = 1

CRAWL_DELAY_SECONDS = 0.5

HEADERS = {
    "User-Agent": "MiniSearchEngineBot/1.0"
}
