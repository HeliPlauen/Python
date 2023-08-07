
import time
import threading


class TestThread(threading.Thread):

    def __init__(self, name='TestThread'):

        # Constructor, setting initial variables 
        self._stopevent = threading.Event()
        self._sleepperiod = 1

        threading.Thread.__init__(self, name=name)

    def run(self):

        # Main control loop 
        print(f"{(self.name)} starts")

        count = 0
        while not self._stopevent.is_set():
            count += 1
            print(f"loop {count}")
            self._stopevent.wait(self._sleepperiod)

        print(f"{self.name} ends")

    def join(self, timeout=None):

        # Stop the thread. 
        self._stopevent.set()
        print("Stop!")
        threading.Thread.join(self, timeout)        


if __name__ == "__main__":
    testthread = TestThread()
    testthread.start()

    time.sleep(10)
    testthread.join()