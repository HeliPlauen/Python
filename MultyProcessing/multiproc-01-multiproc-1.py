
import time
import multiprocessing


def test():
    while True:
        print(f"{multiprocessing.current_process()}", time.time())
        time.sleep(1)


if __name__ == "__main__":
    time.sleep(1)
    multiprocessing.Process(target=test, name="prc-1").start()
    multiprocessing.Process(target=test, name="prc-2").start()
    print("Process started")


