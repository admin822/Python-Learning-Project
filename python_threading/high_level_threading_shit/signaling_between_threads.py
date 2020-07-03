import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s')

def func1(e:threading.Event):
    start_time=time.time()
    logging.info("func1 has started at {0}, waiting for event to proceed".format(start_time))
    e.wait()
    logging.info("func1 has finished at {0}, the whole thread execution took {1} seconds".format(time.time(),time.time()-start_time))

def func2(e:threading.Event,t:int):
    start_time=time.time()
    logging.info("func2 has started at {0}, waiting for event to proceed".format(start_time))
    e.wait(t)
    logging.info("func2 has finished at {0}, the whole thread execution took {1} seconds".format(time.time(),time.time()-start_time))
    if(e.is_set()):
        logging.info("func2 finished due to the change of internal flag")
    else:
        logging.info("func2 exited due to timeout")

def func3(e:threading.Event):
    start_time=time.time()
    logging.info("func3 has started at {0}, waiting for event to proceed".format(start_time))
    time.sleep(3)
    e.set()
    logging.info("func3 has finished at {0}, the whole thread execution took {1} seconds".format(time.time(),time.time()-start_time))

e=threading.Event()
t1=threading.Thread(name="func1",target=func1,kwargs={'e':e})
t2=threading.Thread(name="func2",target=func2,kwargs={'e':e,'t':2})
t3=threading.Thread(name="func3",target=func3,kwargs={'e':e})
t1.start()
t2.start()
t3.start()