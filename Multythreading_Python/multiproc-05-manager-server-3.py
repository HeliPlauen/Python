
import time
import multiprocessing.managers as mult


def get_time():
    return time.time()


mult.BaseManager.register("get", callable=get_time)
manager = mult.BaseManager(address = ('', 4444), authkey = b'abc')
server = manager.get_server()
print("server_start")
server.serve_forever()
