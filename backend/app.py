"""
app.py
------
Flask backend API. Exposes:

  GET /api/search?q=your+query   -> JSON search results
  GET /api/health                 -> simple health check (used by hosting platforms)

Run locally:
    python app.py
Then visit:
    http://localhost:5000/api/search?q=web+crawler
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

from search import search

app = Flask(__name__)

# Allow requests from any origin so the frontend (hosted separately,
# e.g. on GitHub Pages) can call this API. In production you can
# restrict this to your actual frontend domain.
CORS(app)


@app.route("/api/health", methods=["GET"])
def health():
    """Simple endpoint to confirm the API is alive."""
    return jsonify({"status": "ok"})


@app.route("/api/search", methods=["GET"])
def api_search():
    """
    Main search endpoint.
    Example: /api/search?q=information+retrieval&limit=10
    """
    query = request.args.get("q", "").strip()
    limit = request.args.get("limit", 10, type=int)

    if not query:
        return jsonify({"error": "Missing query parameter 'q'"}), 400

    results = search(query, top_k=limit)

    return jsonify({
        "query": query,
        "count": len(results),
        "results": results,
    })


if __name__ == "__main__":
    # debug=True is fine for local development; hosting providers
    # will run this with a production server (e.g. gunicorn) instead.
    app.run(debug=True, port=5000)
