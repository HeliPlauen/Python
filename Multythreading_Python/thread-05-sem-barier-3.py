import time
import threading
import random


def test(barrier):
    slp = random.randint(10, 30)
    time.sleep(slp)
    print(f"Thread{threading.current_thread().name} started at ({time.ctime()})")
    
    barrier.wait()
    print(f"Thread{threading.current_thread().name} overcomed the barrier at ({time.ctime()})")


bar = threading.Barrier(5)

for i in range(5):
    threading.Thread(target=test, args=(bar,), name=f"Thr-{i}").start()
