import http.server
import socketserver

class HelloWorldHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("index.html", "rb") as file:
            self.wfile.write(file.read())

PORT = 8000

with socketserver.TCPServer(("", PORT), HelloWorldHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
