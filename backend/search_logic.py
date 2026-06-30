"""
search.py
---------
Implements BM25 ranking on top of the inverted index built by indexer.py.

BM25 is an improvement over plain TF-IDF. The key intuition:
- A query word that appears in FEWER documents is more important
  (this is the IDF / "inverse document frequency" part).
- A word appearing MORE times in a document makes that document more
  relevant, but with DIMINISHING RETURNS (this is what TF-IDF lacks —
  BM25 fixes it by saturating term frequency).
- Documents that are unusually LONG get a small penalty, since long
  documents naturally contain more word matches by chance.

You don't need to memorize the formula to use this file — just know
it returns better-ranked results than counting word matches.
"""

import json
import math

import config
from indexer import tokenize

# BM25 tuning constants (standard default values used by most search engines)
K1 = 1.5   # Controls how quickly term-frequency saturates
B = 0.75   # Controls how strongly document length is penalized


def load_index():
    """Load the prebuilt index from disk."""
    try:
        with open(config.INDEX_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def bm25_score(term_freq: int, doc_length: int, avg_doc_length: int,
                num_docs_with_term: int, total_docs: int) -> float:
    """
    Compute the BM25 score contribution of a single query term
    for a single document.
    """
    # IDF: rarer terms across the corpus score higher
    idf = math.log(
        (total_docs - num_docs_with_term + 0.5) / (num_docs_with_term + 0.5) + 1
    )

    # TF component with saturation + length normalization
    numerator = term_freq * (K1 + 1)
    denominator = term_freq + K1 * (1 - B + B * (doc_length / avg_doc_length))

    return idf * (numerator / denominator)


def search(query: str, top_k: int = 10):
    """
    Search the index for a query string.
    Returns a list of result dicts sorted by relevance (best first):
        [{"url": ..., "title": ..., "snippet": ..., "score": ...}, ...]
    """
    index_data = load_index()
    if index_data is None:
        return []

    documents = index_data["documents"]
    inverted_index = index_data["inverted_index"]
    avg_doc_length = index_data["avg_doc_length"]
    total_docs = index_data["total_docs"]

    query_terms = tokenize(query)
    if not query_terms:
        return []

    # doc_id -> accumulated BM25 score
    scores = {}

    for term in query_terms:
        postings = inverted_index.get(term)
        if not postings:
            continue  # term doesn't appear in any document

        num_docs_with_term = len(postings)

        for doc_id, term_freq in postings.items():
            doc_length = documents[doc_id]["length"]
            score = bm25_score(
                term_freq, doc_length, avg_doc_length,
                num_docs_with_term, total_docs
            )
            scores[doc_id] = scores.get(doc_id, 0) + score

    # Sort documents by score, descending
    ranked_doc_ids = sorted(scores, key=scores.get, reverse=True)[:top_k]

    results = []
    for doc_id in ranked_doc_ids:
        doc = documents[doc_id]
        results.append({
            "url": doc["url"],
            "title": doc["title"],
            "snippet": doc["snippet"],
            "score": round(scores[doc_id], 4),
        })

    return results


if __name__ == "__main__":
    # Quick manual test from the command line:
    # python search.py
    while True:
        q = input("\n🔍 Search query (or 'quit'): ")
        if q.lower() == "quit":
            break
        results = search(q)
        if not results:
            print("No results found.")
        for i, r in enumerate(results, 1):
            print(f"{i}. {r['title']} (score: {r['score']})")
            print(f"   {r['url']}")
            print(f"   {r['snippet'][:120]}...")
