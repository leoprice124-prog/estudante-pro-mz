import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(os.environ.get("PORT", 3000))

class EstudanteHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        caminho = self.path.split("?").pop(0)
        rotas = {
            "/ads.txt": ("text/plain; charset=utf-8", "ads.txt"),
            "/manifest.json": ("application/manifest+json; charset=utf-8", "manifest.json"),
            "/sw.js": ("application/javascript; charset=utf-8", "sw.js"),
            "/icon-512.png": ("image/png", "icon-512.png")
        }
        if caminho in rotas and os.path.exists(rotas[caminho]):
            ctype, fname = rotas[caminho]
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Service-Worker-Allowed", "/")
            self.end_headers()
            with open(fname, "rb") as f:
                self.wfile.write(f.read())
            return
        if caminho == "/" or not os.path.exists(caminho.lstrip("/")):
            self.path = "/index.html"
        return super().do_GET()

if __name__ == "__main__":
    print(f"Estudante Pro MZ ativo na porta {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), EstudanteHandler).serve_forever()