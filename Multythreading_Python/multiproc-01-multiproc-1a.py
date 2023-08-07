
import time
import multiprocessing


def test():
    while True:
        print(f"{multiprocessing.current_process()}", time.time())
        time.sleep(1)


if __name__ == "__main__":
    time.sleep(1)
    pr = multiprocessing.Process(target=test, name="prc-1")
    pr.start()
    
    print(pr.is_alive())
    print(pr.pid)

    time.sleep(10)
    pr.terminate()




