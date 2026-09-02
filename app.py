from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response = {
            "message": "Hello DevOps",
            "environment": "production",
            "status": "healthy",
            "version": "1.0.0"
        }
        self.wfile.write(json.dumps(response).encode("utf-8"))

def run():
    server_address = ("0.0.0.0", 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server running on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
