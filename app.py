import http.server
import socketserver

class HelloWorldHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello World")

PORT = 8000

with socketserver.TCPServer(("", PORT), HelloWorldHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
