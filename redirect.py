import http.server
import socketserver
import os

PORT = 4323

class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location', 'http://localhost:4322')
        self.end_headers()

with socketserver.TCPServer(('', PORT), RedirectHandler) as httpd:
    print(f'Redirecting {PORT} to 4322')
    httpd.serve_forever()
