
import time
import json
import random
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDRESS = "127.0.0.1"
PORT = 8888
sock.connect((ADDRESS, PORT))


# ERROR!!!!
print("POST:")
ID = random.randint(1, 99999)
request_json = {
    "key":f"REQUEST JSON {str(ID)}"
}
request_content = [
    "POST / HTTP/1.1",
    f"Host: {ADDRESS}",
    "Connection: keep-alive",
    "Accept: text/html",
    "Content-Length: 300", 
    "\n"
]
request = "\n".join(request_content)
sock.send(request.encode())
response = (sock.recv(10024)).decode()
print(response)

# We have not got message!!!!!

print("\n")


time.sleep(10)

