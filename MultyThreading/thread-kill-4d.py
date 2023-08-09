
# SuperFastPython.com
# example of a extending the thread class

from time import sleep
from threading import Thread
 

# custom thread class
class CustomThread(Thread):

    # constructor
    def __init__(self):

        # call the parent constructor
        super(CustomThread, self).__init__()
 
    # execute task
    def run(self):

        # execute a task in a loop
        for i in range(5):

            # block for a moment
            sleep(1)

            # report a message
            print('Worker thread running...')

        print('Worker closing down')
 

# create a new thread
thread = CustomThread()

# start the new thread
thread.start()

# wait for the new thread to finish
thread.join()