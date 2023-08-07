import time
from threading import Thread, BoundedSemaphore, current_thread
import random


max_connections = 5
pool = BoundedSemaphore(max_connections)


def test():
    with pool:
        slp = random.randint(1, 5)
        print(f"{current_thread().name} - sleep({slp})")
        time.sleep(slp)


for i in range(10):
    Thread(target=test, name=f"Thr-{i}").start()
