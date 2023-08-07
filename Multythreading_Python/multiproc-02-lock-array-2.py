
import time
import random
import multiprocessing


def add_value(locker, array, index):
    with locker:
        num = random.randint(0, 20)
        vtime = time.ctime()
        array[index] = num
        print(f"array[{index}] = {num}, time = {vtime}")
        time.sleep(num)


lock = multiprocessing.Lock()
arr = multiprocessing.Array("i", range(10))
processes = []


if __name__ == "__main__":
    for i in range(10):
        pr = multiprocessing.Process(target=add_value, args=(lock, arr, i))
        processes.append(pr)
        pr.start()


    for proc in processes:
        proc.join()


    print(list(arr))




