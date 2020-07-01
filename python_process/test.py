import threading
import time
import multiprocessing

def func1():
    print("this is a test")
    time.sleep(1)
    print("test ended")

start_time=time.time()
p1=multiprocessing.Process(target=func1)
p2=multiprocessing.Process(target=func1)
p3=multiprocessing.Process(target=func1)
p1.start()
print("ended in {} seconds".format(time.time()-start_time))