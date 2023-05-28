dict={'name':'pradip','surname':'kachhadiya','middelname':'chimanbhai'}
dict['std']=13
# dict.year=2020
d=dict.get('surname',-1)
print(d)
print(dict.items())
k=input('Enter Your Key')
v=input('Enter Your Value')
dict.update({k:v})
print(dict)
# ======================================SORT==========================================
dict={10:'pradip',1:'kachhadiya',6:'chimanbhai',30:'hello'}
c1=sorted(dict.items(),key=lambda t: t[0])
c2=sorted(dict.items(),key=lambda t: t[1])
print(c1)
print(c2)
================================LIST INTO DICTIONARY==================================
s=['name','surname','middelname','std']
k=['pradip','kachhadiya','chimanbhai',12]
n=list(zip(s,k))
print(n)
j=dict(n)
print(j)
for i in j:
    print(f'{i}--------{j[i]}')

==============================DICTIONARY PASS THROW FUNCTION==========================

def dict(dictionary):
    for i,j in dictionary.items():
        print(i,'----------------',j)
m={'h':5,'k':8,"j":9}        
h=dict(m)
================================ORDER LIST===========================
from collections import OrderedDict
d=OrderedDict()
d['j']=4
d['k']=2
d['h']=6
for i,j in d.items():
    print(i,'-----------------',j)