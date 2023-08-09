

# SuperFastPython.com
# !!!! USING PROCESS TRMINATE !!!!

from random import random
from time import sleep
from threading import Thread

# !!!!!!!!!!!!!!!!!!!!!!!!!!!
import multiprocessing 

# task function
def task():

    # loop forever
    while True:

        # generate a random value between 0 and 1
        value = random()
        print(f'.{value}')

        # block
        sleep(value)

        # check if we should forcefully close the thread
        if value > 0.9:
            print('Closing thread')
            
            # !!!!!!!!!!!
            # get the current process
            process = multiprocessing.current_process()
            print(process.name)

            # kill the process
            #process.terminate()
            process.kill()
 

# create and configure the new thread
thread = Thread(target=task)

# start the new thread
thread.start()

# wait for the thread to terminate
thread.join()

# main continues on
print('Main continuing on...')