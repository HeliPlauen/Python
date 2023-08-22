
# SuperFastPython.com
# example of stopping a custom thread class

from time import sleep
from threading import Thread
from threading import Event
 

# custom thread class
class CustomThread(Thread):

    # constructor
    def __init__(self, event):

        # call the parent constructor
        super(CustomThread, self).__init__()

        # store the event
        self.event = event
 
    # execute task
    def run(self):

        # execute a task in a loop
        while True:

            # block for a moment
            sleep(1)

            # check for stop
            if self.event.is_set():
                print("Stopped!")
                break

            # report a message
            print('Worker thread running...')

        print('Worker closing down')
 

# create the event
event = Event()

# create a new thread
thread = CustomThread(event)

# start the new thread
thread.start()

# block for a while
sleep(5)

# stop the worker thread
print("Here must be SET!!!")
#event.set()

# wait for the new thread to finish
thread.join()
print('Main stopping thread')