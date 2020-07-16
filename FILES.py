===================write the file=================
f = open('myfile.txt','w')
str=input('Enter Your Full bio ')
f.write(str)
f.close()

===================READ FILE======================
f = open('myfile.txt','r')
j=f.read()
print(j)
f.close()

=====================APPEND FILE====================
f = open('myfile.txt','a')
str=input('Enter Your Full bio ')
f.write(str)
f.close()

====================WRITE INSIDE OLD FILE============
f = open('myfile.txt','w')
str=input('Enter Your Full bio ')
f.write(str)
f.close()

======================>>w+ MODE<<======================
f = open('myfile.txt','w+')
s=f.read()
print(s)
str=input('Enter Your Full bio ')
f.write(str)
f.close()

===========================>r+<===========================
f = open('myfile.txt','r+')
s=f.read()
print(s)
str=input('Enter Your Full bio ')
f.write(str)
f.close()

============================>a+<=============================
f = open('myfile.txt','a+')
str=input('Enter Your Full bio ')
f.write(str)
f.seek(0,0)
s=f.read()
print(s)
f.close()

========================FILE EXIST OR NOT=======================
import os,sys
fname=input("Enter your file name ")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print('oppps!!! you are enter wrong file name') 
    sys.exit()
g=f.read()
print(g)
f.close() 

=========================>WITH STATEMENT<============================
with open('myfile.txt','r') as f:
    g=f.read()
    print(g)

===========================>BINARY FILE<===============================
f1=open('god.jpg','rb')
f2=open('myfile.text','wb')
h=f1.read()
f2.write(h)
f1.close()
f2.close()

==============================>PICKLE FILE<================================

import pickle
class person:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def display(self):
        print(f"id:{self.id:5d}-----name:{self.name}-----salary:{self.sal}") 
        
f=open('myfile2.txt','wb')
n=int(input("How many Employ Add? "))
for i in range(n):
    id=int(input("Enter Id No. : ")) 
    name=input("Enter Name : ")
    salary=input("Enter Salary : ") 
    p=person(id,name,salary)
    pickle.dump(p,f) 
f.close() 

f=open('myfile2.txt','r+b')
while True:
    try:
         obj=pickle.load(f)
         obj.display()
    except EOFError:
        break     

=====================ENCODE AND DECODE FILE========================
name="pradip\n"
with open('myfile2.txt','wb') as f:
    f.write(name.encode())
    f.write(b"hello")
    
with open('myfile2.txt','rb') as f:
    k=f.read() 
    print(k.decode())  

==========================>ZIPPING AND UNZIPPING<======================== 

from zipfile import *
f = ZipFile('test1.zip','w',ZIP_DEFLATED)
f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')
f.close()

===============UNZIPPING=============
j=ZipFile('test1.zip','r')
j.extractall()

===============================> READLINE OR READLINES METHOD <===============================
with open('gmail.txt','r') as f:
    h=f.readline()
    h1=f.readlines()
    print(h)
    print(h1)
    
===============================>SEEK AND TELL METHOD<======================================
with open('gmail.txt','a') as f:
    print(f.tell())
    f.seek(0,0)
    print(f.tell())
    
  

    


    