import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(os.environ.get("PORT", 3000))

class EstudanteHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        caminho = self.path.split("?").pop(0)
        if caminho == "/ads.txt":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"google.com, pub-6467621234967556, DIRECT, f08c47fec0942fa0")
            return
        if caminho == "/manifest.json":
            self.send_response(200)
            self.send_header("Content-Type", "application/manifest+json; charset=utf-8")
            self.end_headers()
            with open("manifest.json", "rb") as f:
                self.wfile.write(f.read())
            return
        if caminho == "/sw.js":
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript; charset=utf-8")
            self.end_headers()
            with open("sw.js", "rb") as f:
                self.wfile.write(f.read())
            return
        if caminho == "/" or not os.path.exists(caminho.lstrip("/")):
            self.path = "/index.html"
        return super().do_GET()

if __name__ == "__main__":
    print(f"Estudante Pro MZ App ativo na porta {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), EstudanteHandler).serve_forever()