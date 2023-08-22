
import time
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDRESS = "127.0.0.1"
PORT = 8888
sock.connect((ADDRESS, PORT))

print("GET:")
request_content = [
    "GET / HTTP/1.1",
    f"Host: {ADDRESS}",
    "Connection: keep-alive",
    "Accept: text/html",
    "\n"
]
request = "\n".join(request_content)
sock.send(request.encode())
response = (sock.recv(10024)).decode()
print(response)

# We have not got message!!!!!


time.sleep(10)

