import random
import time
from concurrent.futures.thread import ThreadPoolExecutor
import concurrent.futures
executor=ThreadPoolExecutor(10)
def concurrents(fn):
    def wrapper(*args,**kwargs):
        return executor.submit(fn,*args,**kwargs)
    return wrapper


@concurrents
def func1(id:int):
    print("unthreaded process {} started".format(id))
    time.sleep(5)
    print("unthreaded process {} ends".format(id))

thread=func1(1)
while(not thread.done()):
    pass
print("finished")
    



# @concurrents
# def func2(id:int):
#     print("threaded process {} started".format(id))
#     time.sleep(1.5)
#     print("threaded process {} ends".format(id))


# if __name__ =="__main__":
#     ids=[1,2,3,4,5]
#     start_time=time.time()
#     for id in ids:
#         func1(id)
#     print("unthreaded thread ended in {} seconds".format(time.time()-start_time))

#     start_time=time.time()
#     threads=[]
#     for id in ids:
#         threads.append(func2(id))
#     results= concurrent.futures.as_completed(threads)
#     for r in results:
#         r.result()
#     print("threaded threads ended in {} seconds".format(time.time()-start_time))


# class test_class:
#     def __init__(self):
#         self.threads=[]

#     @concurrents
#     def func3(self,id:int):
#         print("threaded process {} started".format(id))
#         time.sleep(1.5)
#         print("threaded process {} ends".format(id))    
    
#     def func4(self,id:int):
#         self.threads.append(self.func3(id))
#         results=concurrent.futures.as_completed(self.threads)
#         for r in results:
#             r.result()

# t1=test_class()
# start_time=time.time()
# for id in ids:
#     t1.func3(id)
# print("finished in {} seconds".format(time.time()-start_time))
        