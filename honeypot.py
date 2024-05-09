import socket
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import re
import datetime

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>31313131313131.</h1></body></html>")
        # Gelen GET isteğini raporla
        raporla(f"GET isteği: {self.client_address[0]} - {self.path}")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST verisi.")
        raporla(f"POST isteği: {self.client_address[0]} - {post_data.decode()}")

    def log_message(self, format, *args):
        return

def run_web_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print(f"Web sunucusu çalışıyor: http://localhost:{port}")
    httpd.serve_forever()

def handle_connection(client_socket, address):
    try:
        print(f"Bağlantı kabul edildi: {address}")
        while True:
            veri = client_socket.recv(1024)
            if not veri:
                break
            print(f"{address} adresinden gelen veri: {veri.decode()}")
            # Gelen veriyi analiz edip saldırı tespitini raporla
            if re.search(r'(SELECT|INSERT|UPDATE|DELETE|DROP|ALTER|CREATE)', veri.decode(), re.IGNORECASE):
                raporla(f"SQL Enjeksiyon Saldırısı: {address} - {veri.decode()}")
            
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        client_socket.close()

def raporla(mesaj):
    tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("raporlar.txt", "a") as dosya:
        dosya.write(f"[{tarih}] {mesaj}\n")

port_web = 80
port_honeypot = int(input("Honeypot için dinlenecek portu girin: "))

web_thread = threading.Thread(target=run_web_server, args=(port_web,))
web_thread.start()

soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soket.bind(('0.0.0.0', port_honeypot))
soket.listen(5)
print(f"Honeypot dinlemeye başladı: {port_honeypot}")

while True:
    client_socket, address = soket.accept()
    t = threading.Thread(target=handle_connection, args=(client_socket, address))
    t.start()
