"""
api/search.py
--------------
This file becomes your live API endpoint automatically.
Once deployed on Vercel, this is reachable at:  /api/search?q=yourquery
"""

import json
import sys
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

from search_logic import search  # noqa: E402


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        query = query_params.get("q", [""])[0].strip()
        limit = int(query_params.get("limit", ["10"])[0])

        if not query:
            response_body = {"error": "Missing query parameter 'q'"}
            status_code = 400
        else:
            results = search(query, top_k=limit)
            response_body = {
                "query": query,
                "count": len(results),
                "results": results,
            }
            status_code = 200

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(response_body).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
