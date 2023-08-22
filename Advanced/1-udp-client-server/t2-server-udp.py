
import socketserver


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        #print(data)
        #print(data.decode())
        #print(socket)
        print(f"Connection with ID:{data.decode()} detected!!!")
        response_data = f"pocessed: {data.decode()}"
        socket.sendto(bytes(response_data, "utf-8"), self.client_address)


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8888
    with socketserver.UDPServer((HOST, PORT), UDPHandler) as server:
        server.serve_forever()

