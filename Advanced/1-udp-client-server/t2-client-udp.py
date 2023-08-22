
import socket
import random
import time


stringID = str(random.randint(1, 99999))
bytesID = bytes(stringID, "utf-8")

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
skt.sendto(bytesID, ("127.0.0.1", 8888))
response = skt.recv(1024)
print(f"Response: {response.decode()}")
time.sleep(10)
