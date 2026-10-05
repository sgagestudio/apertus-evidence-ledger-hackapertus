from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        if self.path != "/v1/chat/completions":
            self.send_error(404)
            return

        length = int(self.headers.get("content-length", "0"))
        payload = json.loads(self.rfile.read(length))
        system = payload["messages"][0]["content"]

        if "evidence sufficiency gate" in system:
            model_content = json.dumps({"supported": True})
        else:
            model_content = json.dumps(
                {
                    "answer": "Operational incident records are retained for 90 days after closure.",
                    "abstain": False,
                    "citations": [
                        {
                            "chunk_id": 1,
                            "quote": "Operational incident records are retained for 90 days after closure.",
                        }
                    ],
                }
            )

        body = json.dumps(
            {"choices": [{"message": {"role": "assistant", "content": model_content}}]}
        ).encode("utf-8")
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args) -> None:
        return


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
