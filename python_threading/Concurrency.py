import threading
import time



class test_class:
    def __init__(self):
        self.threads=[]

    def func(self,secs:int):
        print("func started")
        time.sleep(secs)
        print("func ended in {} seconds".format(secs))

    def thread_func(self,secs:int):
        self.threads.append(threading.Thread(target=self.func(secs)))
        for t in self.threads:
            t.join()


tc=test_class()

start_time=time.time()
times=[5,6,7,8,9]
for t in times:
    tc.thread_func(t)
end_time=time.time()
print("func fininshed in {}".format(end_time-start_time))
