
# Python program killing
# a thread using ._stop()
# function
 
import time
import threading
 

class MyThread(threading.Thread):
 
    # Thread class with a _stop() method.
    # The thread itself has to check
    # regularly for the stopped() condition.
 
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._stopper = threading.Event()                # Here was a mistake
 
    # function using _stop function
    def stop(self):
        self._stopper.set()                              # Here was a mistake
 
    def stopped(self):
        return self._stopper.is_set()                    # Here was a mistake
 
    def run(self):
        while True:
            if self.stopped():
                return
            print("Hello, world!")
            time.sleep(1)
 

t1 = MyThread() 
t1.start()
time.sleep(5)
t1.stop()
time.sleep(1)
t1.join()