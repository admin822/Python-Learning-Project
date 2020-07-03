import threading

class water_molecule_generator:
    def __init__(self):
        self.event=threading.Event()
        self.finished=threading.Event()
        self.event.clear()
        self.hy_queue=[]
        self.ox_queue=[]
        self.t=threading.Thread(target=self.generator,daemon=True)
        self.t.start()

    def generator(self):
        while(self.finished.is_set()==False):
            if(len(self.hy_queue)>=2 and len(self.ox_queue)>=1):
                self.hy_queue.pop().start()
                self.ox_queue.pop().start()
                self.hy_queue.pop().start()
        print("the generator has stopped")

    def _release_hydrogen(self):
        print('H')
    def _release_oxygen(self):
        print('O')
    def hydrogen(self):
        t=threading.Thread(target=self._release_hydrogen)
        self.hy_queue.append(t)
    def oxygen(self):
        t=threading.Thread(target=self._release_oxygen)
        self.ox_queue.append(t)
    def destroy(self):
        self.finished.set()

if __name__=="__main__":
    water_gen=water_molecule_generator()
    s=threading.Semaphore(2)
    while(True):
        try:
            print(threading.enumerate())
            print("please give the next command")
            cmd=input()
            if(cmd=='h' or cmd=='H'):
                water_gen.hydrogen()
            elif(cmd=='o' or cmd=="O"):
                water_gen.oxygen()
        except KeyboardInterrupt:
            #water_gen.destroy()
            break



