
import time
import multiprocessing.managers as mult


mult.BaseManager.register("get")
manager = mult.BaseManager(address = ('127.0.0.1', 4444), authkey = b'abc')
print("client_connected")
manager.connect()

res = manager.get()
print(f"result: {res}")
time.sleep(10)
