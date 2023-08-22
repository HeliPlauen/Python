
import time
import json
import requests
import random


response = requests.get('http://127.0.0.1:8888')
print("GET:")
print(f"Status code: {response}")
print(f"URL: {response.url}")
print(f"Headers: {response.headers}")
print(f"Body: {response.text}")
print("\n")


time.sleep(1)


print("POST1:")
ID = random.randint(1, 99999)
request_json = {
    "key":f"REQUEST JSON {str(ID)}"
}
response = requests.post(
    'http://127.0.0.1:8888', 
    json=request_json,
)
print(f"Status code: {response}")
print(f"URL: {response.url}")
print(f"Headers: {response.headers}")
print(f"Body: {response.text}")
print("\n")


time.sleep(1)


print("POST2:")
ID = random.randint(1, 99999)
request_data = {
    "key": f"REQUEST DATA {str(ID)}"
}
response = requests.post(
    'http://127.0.0.1:8888', 
    data=json.dumps(request_data)
)
print(f"Status code: {response}")
print(f"URL: {response.url}")
print(f"Headers: {response.headers}")
print(f"Body: {response.text}")
print("\n")


time.sleep(10)

