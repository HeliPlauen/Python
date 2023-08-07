
import time
import multiprocessing


cond = multiprocessing.Condition()


def f1(cond):
    while True:
        with cond:
            cond.wait()
            print("Get event")


def f2(cond):
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print(f"f2: {i}")
        time.sleep(1)



if __name__ == "__main__":
    multiprocessing.Process(target=f1, args=(cond,)).start()
    multiprocessing.Process(target=f2, args=(cond,)).start()


