import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s')

class counter:
    def __init__(self):
        self.lock=threading.Lock()
        self.counter=0
    def increment(self):
        logging.info("trying to acquire lock")
        acquired=self.lock.acquire(timeout=1)
        if(acquired):
            time.sleep(0.5)
            self.counter+=1
            logging.info(self.counter)
            self.lock.release()
        else:
            logging.info("current thread exited due to timeout")

c1=counter()
for i in range(5):
    t=threading.Thread(target=c1.increment)
    t.start()
