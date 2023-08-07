
import time
import multiprocessing


lock = multiprocessing.RLock()


def get_value(l):
    l.acquire()                                         # We can NOT UNlock it from everywhere  (from any other thread)   
    pr_name = multiprocessing.current_process().name    
    print(f"Process [{pr_name}] - started!!! ({time.time()})")


def unloc_process(l):  
    try:
        time.sleep(10)
        l.release() 
        print(f"Unlocked!  ({time.time()})")    
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    multiprocessing.Process(target=get_value, args=(lock,), name="pr-1").start()
    multiprocessing.Process(target=get_value, args=(lock,), name="pr-2").start()
    multiprocessing.Process(target=unloc_process, args=(lock,), name="unlocker").start()  # Not Successfull attempt to unlock!!!!





