
import time
import multiprocessing


def test():
    for i in range(5):
        print(f"{multiprocessing.current_process()}", time.time())
        time.sleep(1)


prc = []


if __name__ == "__main__":
    for _ in range(5):
        pr = multiprocessing.Process(target=test)
        prc.append(pr)
        pr.start()

    for pr in prc:
        pr.join()    

    print("All processes were finished!!")





