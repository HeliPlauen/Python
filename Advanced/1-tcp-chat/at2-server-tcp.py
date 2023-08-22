
import json
import socketserver


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        dict_data = json.loads(data.decode())
        print(f"{dict_data['userID']}: {dict_data['message']}")
        self.request.sendall(b"OK")


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8888
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()

