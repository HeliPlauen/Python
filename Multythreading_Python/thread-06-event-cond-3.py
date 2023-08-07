
import time
import threading


cond = threading.Condition()


def f1():
    while True:
        with cond:
            cond.wait()
            print("Event was gotten")


def f2():
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print(f"f1 - {i}")
        time.sleep(1)


threading.Thread(target=f1).start()
threading.Thread(target=f2).start()