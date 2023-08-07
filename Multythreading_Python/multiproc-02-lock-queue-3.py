
import time
import random
import multiprocessing


def get_text(que):
    val = random.randint(0, 10)
    que.put(str(val))


queue = multiprocessing.Queue()
pr_list = []


if __name__ == "__main__":
    for _ in range(10):
        pr = multiprocessing.Process(target=get_text, args=(queue,))
        pr_list.append(pr)
        pr.start()

    for proc in pr_list:
        proc.join()
    
    for elem in iter(queue.get, None):
        print(elem)




