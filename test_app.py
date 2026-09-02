import unittest
from http.server import HTTPServer
import threading
import urllib.request
import json
from app import SimpleHandler

class TestWebServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(('127.0.0.1', 8081), SimpleHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_health_check(self):
        url = 'http://127.0.0.1:8081'
        with urllib.request.urlopen(url) as response:
            self.assertEqual(response.status, 200)
            payload = json.loads(response.read().decode('utf-8'))
            self.assertEqual(payload.get("message"), "Hello DevOps")
            self.assertEqual(payload.get("status"), "healthy")

if __name__ == '__main__':
    unittest.main()
