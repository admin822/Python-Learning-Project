import multiprocessing
import random
import time
import threading
def func1():
    print("processing of {} numbers started".format(10000))
    for _ in range(10000):
        a=random.randint(1,10)
        b=random.randint(1,10)
        a+b*a/b+pow(a,b)-a+b*pow(a,b)-pow(a,b)
    print("processing of {} numbers has ended".format(10000))

def func2():
    print("processing of {} numbers started".format(1000))
    for _ in range(1000):
        a=random.randint(1,10)
        b=random.randint(1,10)
        a+b*a/b+pow(a,b)-a+b*pow(a,b)-pow(a,b)
    print("processing of {} numbers has ended".format(1000))

start_time=time.time()
func1()
print("single process end in {} seconds".format(time.time()-start_time))

start_time=time.time ()
processes=[]
for _ in range(10):
    p=multiprocessing.Process(target=func2)
    p.start()
    processes.append(p)
for p in processes:
    p.join()
print("multiprocessing ended in {} seconds".format(time.time()-start_time))

# start_time=time.time()
# threads=[]
# for i in range(10):
#     t=threading.Thread(target=func2)
#     t.start()
#     threads.append(t)
# for t in threads:
#     t.join()
# print("multithreading ended in {} seconds".format(time.time()-start_time))