
import socket
import time
import json


skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect(('localhost', 8888))

userID = "Oleg"
message = input("Message: ")
dict_data = {"userID": userID, "message": message}
str_data = json.dumps(dict_data)
data = bytes(str_data, "utf-8")
skt.send(data)

response = skt.recv(64)
print(f"Response: {response.decode()}")
skt.close()
time.sleep(5)
