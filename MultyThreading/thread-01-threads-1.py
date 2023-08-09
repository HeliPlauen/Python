
import threading
import time


def get_data(data):
    while True:
        print(f"[{threading.currentThread().name}] - {data}")
        time.sleep(5)

thr = threading.Thread(target=get_data, args=(str(time.time()),), name="thr-1")
thr.start()

for i in range(100):
    print(f"current: {i}")
    time.sleep(1)

    if i % 10 == 0:
        print(f"Active thread: {threading.active_count()}")
        print(f"Enumerate: {threading.enumerate()}")
        print(f"thr-1 is alive: {thr.is_alive()}")