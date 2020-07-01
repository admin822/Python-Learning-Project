from concurrent.futures.process import ProcessPoolExecutor
import concurrent.futures
import time
import os
import random
executor=ProcessPoolExecutor()

def func1():
    print("processing of {} numbers started".format(100000))
    for _ in range(100000):
        a=random.randint(1,10)
        b=random.randint(1,10)
        a+b*a/b+pow(a,b)-a+b*pow(a,b)-pow(a,b)
    print("processing of {} numbers has ended".format(100000))

def func2():
    print("processing of {} numbers started".format(1000))
    for _ in range(1000):
        a=random.randint(1,10)
        b=random.randint(1,10)
        a+b*a/b+pow(a,b)-a+b*pow(a,b)-pow(a,b)
    print("processing of {} numbers has ended".format(1000))

if __name__ =="__main__":
    start_time=time.time()
    func1()
    print("single process finished in {} seconds".format(time.time()-start_time))

    start_time=time.time()
    processes=concurrent.futures.as_completed([executor.submit(func2) for i in range(100)])
    for p in processes:
        p.result()
    print("multiprocessing finished in {} seconds".format(time.time()-start_time))
