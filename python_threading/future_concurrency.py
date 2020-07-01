import concurrent.futures.thread
from concurrent.futures.thread import ThreadPoolExecutor
import time
import logging
executor=ThreadPoolExecutor()


def func1(seconds:int):
    print("This thread will sleep {} seconds".format(seconds))
    time.sleep(seconds)
    print("This thread has finished in {} seconds".format(seconds))
    return seconds
def add(a:int):
    print(a+1)

secs=[1,2,3,4,5]
secs=secs[::-1]
#####################################first block#############################################
print("#####################################first block#############################################")
start_time=time.time()
threads=[executor.submit(func1,sec) for sec in secs]
print(threads[0])
for t in threads:
    add(t.result())
end_time=time.time()
print("the whole process finished in {} seconds".format(end_time-start_time))
print("#####################################first block#############################################")
#####################################first block#############################################

#####################################second block#############################################
print("#####################################second block#############################################")
second_start_time=time.time()
another_bunch_of_threads=[executor.submit(func1,sec) for sec in secs]
futures=concurrent.futures.as_completed(another_bunch_of_threads)
for f in futures:
    add(f.result())
second_end_time=time.time()
print("Second process end in {} seconds".format(second_end_time-second_start_time))
print("#####################################second block#############################################")
#####################################second block#############################################

#####################################third block#############################################
print("#####################################third block#############################################")
third_start_time=time.time()
third_bunch_of_threads=executor.map(func1,secs)
for result in third_bunch_of_threads:
    add(result)
third_end_time=time.time()
print("Third process end in {} seconds".format(third_end_time-third_start_time))
print("#####################################third block#############################################")
#####################################third block#############################################

