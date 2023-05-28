# ======================== SINGLE THREADING ================
import threading
from time import *
if threading.current_thread()==threading.main_thread():
    print("This is main thread... ")
else:
    print("Oops!!!! your thread is not main thread....")    
    
# ==========================MULTY TASKING THTREADING ==========
from threading import *
def trd():
    print("Hello....") 

for i in range(6):
    t = Thread(target=trd) 
    t.start()

# ========WITH ARG============
def trd(i):
    print("Hello....",i) 
for i in range(6):
    t = Thread(target=trd,args=(i,)) #or===>>>args={i}
    t.start()


# ==================== USING CLASS METHOD ===============
class mythread(Thread):
    def run(self):
        for i in range(6):
            print(i)
            # sleep(0.3)
            
p = mythread()
p.start()
# p.join()
p1=mythread()
p1.start()
       
class mythread(Thread):
    def __init__(self,str):
        Thread.__init__(self)
        self.str=str
        
    def run(self):
        print(self.str)
        for i in range(6):
            print(i)

p1 = mythread("This is 1")
p1.start()
# p1.join()
p2=mythread("This is 2")
p2.start()

# =============================== THREAD SYNCHRONIZATION =================================
class railway:
    def __init__(self,available):
        self.available=available
        self.l=Lock()
        
    def reserve(self,wanted):
        self.l.acquire()
        print("Available seet ",self.available)
        if self.available>=wanted:
            h=current_thread().getName()
            print(wanted,"allotted",h)   
            self.available-=wanted
        else:
            print("Sorry, not available seet..") 
        self.l.release()
p=railway(1)
t1=Thread(target=p.reserve,args=(1,))
t2=Thread(target=p.reserve,args=(1,))  

t1.setName("Person 1")
t2.setName("Person 2")  

t1.start()
# t1.join()       OR======>>>>>>
t2.start()