
============================= TIME =======================
from datetime import * 
epoch = time.time()
print(epoch)
t=time.ctime()
print(t)


============================= DATETIME ======================
now = datetime.now()
dt=date.today()
print(dt)
print(now)
print(now.day,'/',now.month,'/',now.year)
print(now.hour,':',now.minute,':',now.second)
print(dt.strftime("%Z(UTC)"))

=========================RANDOM=======================
import random,time
for i in range(10):
    now = datetime.now()
    print(now.hour,':',now.minute,':',now.second)
    # r=random.randrange(1,100,3)
    # print(r)
    time.sleep(2)

============================== TIME MESURNMENT ===================
from time import *
t1 = perf_counter()
sum = 0
for i in range(1000000):
    sum+=i
# sleep(3)
t2 = perf_counter()
print("This program execution time",t2-t1)    

============================ CALENDAR ==================================
from calendar import *
yy = int(input("Enter year : "))
mm = int(input("Enter month : "))
str = month(yy,mm)
print(str)