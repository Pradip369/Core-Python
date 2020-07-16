1=>>>>>>>CLASSES AND OBJECTS
2=>>>>>>>ENCAPSULATION=======>>>>>It's means  bind the method iside the class...
3=>>>>>>>ABSTRACTION AND INTERFACES
4=>>>>>>>INHERITANCE
5=>>>>>>>POLYMORPHISM

=============================================================================================
====================================>[1]CLASS AND OBJECT<===================================
==============================================================================================
==============================================>DEMO<=========================================

class Student:
    # This is a static or class variable
    pi=3.14
    # This is a constructor
    def __init__(namespace,n="null",m="0"):
        # This is a instance variable
        namespace.name=n
        namespace.mark=m
        print('constructor is called')
    # This is instance method
    def display(namespace):
        print('your name is ',namespace.name) 
        print('your marks is ',namespace.mark)
# class OBJECT
s=Student()
s.display()
print('-------------------------------') 
# class secound object 
s1=Student(n='pradip',m=34)  
s1.display()
print('-------------------------------')

==================================>[1]INSTANCE VARIABLE<======================================

class sample:
    def __init__(namespace):
        namespace.num=10
        print('constructor is called')
        
    def modify(namespace):
        namespace.num+=1

s=sample()
print(s.num)

s1=sample()
s1.modify()
print(s1.num)

print(s.num) 

=============================>[2]CLASS VARIABLE OR STATIC VARIABLE<===========================          
  
class sample:
    x=10
    @classmethod
    def modify(cls):
        cls.x+=1
        
s=sample()
s1=sample()
print(s.x)
print(s1.x)

s.modify()
print(s.x)
print(s1.x)

=======================================>NAMESPACES<=========================================

[1]
class namespace:
    x=19
print(namespace.x)
namespace.x+=1
print(namespace.x)
s=namespace()

[2]
class namespace:
    x=19
s=namespace()
print(s.x)
s.x+=1
print(s.x)
print(namespace.x)

===================================>TYPE OF METHOD<=======================================

=====================================>[1].INSTANCE METHOD<======================================

[1]
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('Hiii',self.name)
        print('Your marks is ',self.marks)
    def calculate(self):
        if self.marks>=80:
            print('First class')
        elif self.marks>=60:
            print('Second class')
        elif self.marks>=40:
            print('Third class')
        else:
            print('You Fail')  
    
n=int(input("How many student? "))
i=0
for i in range(n):
    name=input("Enter student name ") 
    marks=int(input("Enter marks "))
    print("-------------------------------------------------------")
    s=Student(name,marks) 
    s.display()
    s.calculate()
    print("--------------------------------------------------------")
    i+=1 

[2].GETNAME AND SETNAME(MUTATOR METHOD AND ACCESSOR METHOD)

class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
s=Student()
s.setName('pradip')  
print("Your name is ",s.getName()) 

=======================================>[2].CLASS METHOD<======================================

class Bird:
    wings=2
    
    @classmethod
    def fly(cls,name):
        print('This bird name is ',name,' and they have',cls.wings,"wings.") 
        
s=Bird()
s.fly("sparrow")  

====================================>[3].STATIC METHOD<==========================================   
    
class Static:
    n=0
    def __init__(self):
        Static.n+=1
    @staticmethod
    def count():
        print("yor itretion id is",Static.n) 
s=Static()
s1=Static()
s2=Static()
s3=Static()
Static.count()
       
================================>INNER FUNCTION<=========================================
class Outer:
    def msg(self):
        print('Hello pradip this is outer class')
    class Inner:
        def msg(self):
            print('This is inner class')
s=Outer()
s.msg() 
s1=Outer().Inner()
s1.msg()

===========================================================================================
=========================================>INHARITANCE <=====================================
===========================================================================================

=========================================SUPER METHOD=======================================
======SINGLE INHERITANCE========
class Father:
    def __init__(self,property,mony):
        self.property=property
        self.mony=mony
    def sum(self):
        print("father property",self.property)
    def add(self):
          print("This is a super method function")
          
class Son(Father):
    def __init__(self,property2,property,mony):
        super().__init__(property,mony)
        self.property2=property2
        super().add()
    def sum(self):
        print('son property',self.property+self.property2,'and mony is ',self.mony)
 
s=Son(1000,2000,500)
s.sum()

==============MALTIPAL INHERITANCE============
class A(object):
    def hii(self):
        print('This is class a')
class B(object):
    def __init__(self):
        print("This is class b constructor")
    def hii(self):   
        print('This is class b')
class C(object):
    def hii(self):
        print("This is class c") 
class D(C,A,B):
    def hello(self):
        print('this is class inner d')
        # super().__init__()
        super().hii()
    print('This is class outer d')
e=D()
e.hello()

=============================================================================================
========================================>POLYMORPHISM<========================================
============================================================================================== 

==========[1].DUCK TYPING PHILOSOPHY============
class duck:
    def talk(self):
        print('quack...quack...!!!!!')
        
class human:
    def talk(self):
        print('hello.....hii....')
        
def all_talk(obj):
    obj.talk()
    
o=human()
all_talk(o) 
o1=duck()
all_talk(o1)

=============[2].OPERATOR OVERLODING============
class bookx:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
         return self.pages+other.pages
class booky:
    def __init__(self,pages):
        self.pages=pages
b1=bookx(200) 
b2=booky(300)
print(b1+b2)   

==============[3].METHOD OVERLODING =================
class sdd:
    def ----           
            if ------
                ----
            elif  -----:
                ----
            elif -----:
                ------
            else:
                -------
                
==================[4].METHOD OVERRIDING==============
import math as mt                                   
class square:
    def area(self,x):
        print(x*x)
class circle(square):
    def area(self,x):
        print(x*x*mt.pi)
d=square()
d.area(2)
c=circle()
c.area(2)

==============================================================================================
=======================================>ABSTARCT CLASSES<====================================
==============================================================================================

from abc import *
class car(ABC):
    def __init__(self,gear):
        self.gear=gear
    
    def info(self):
        print('this is a best car for this year ')
        print("this car have",self.gear,"gear")
    
    @abstractmethod
    def steering(self):
        pass
    
    @abstractmethod
    def fualtank(self):
        pass
                 
class neno(car):
    def steering(self):
        print("they have flexible steering")
    def fualtank(self):
        print("they have two fual tank") 
j=neno(5)
j.info()
j.steering()
j.fualtank() 
                                    

                    
       
                 

               
            
                        




    