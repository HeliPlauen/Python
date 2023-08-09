
import time
import multiprocessing


class Process(multiprocessing.Process):
    def run(self):
        print("Work!")


if __name__ == "__main__":
    pr = Process()
    pr.start()





