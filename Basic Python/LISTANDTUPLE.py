x=[]
n=int(input("enter element  no."))
for i in range(n):
    a=int(input('enter element'))
    x.append(a)
print(x)
f=[8,6,4,5,5,4,2,4,7,6,3,5,7]
f.sort()
{print(f)
x=(2,3,4,'pradip',True,55,4)
y=(4,5,6,7,4,2,4,7,8)
print(x)
print(x.count(4))
print(max(y))
print(min(y))
# print(x.index(4,3,7))
z=[[2,3,4,5],[4,54,47,55,8,55,5]]
# print(z[1][4])
=========================================ADD ELEMENT==========================
x=(2,3,4,5,67,4,43,8)
p=int(input("Enter position"))
n=[int(input('Enter new no.'))]
new=tuple(n)
print(new)
n1=x[0:p-1]+new
print(n1)
n2=n1+x[p:]
print(n2)
============================================DELETE ELEMENT========================
x=(2,3,4,5,67,4,43,8)
p=int(input("Enter position"))
n1=x[0:p-1]
print(n1)
n2=n1+x[p:]
print(n2)

==================================LIST COMPRIHENSION================================

lst = [i**3 if i%2==0 else i**2 for i in range(1,21)]
lst1= [i**3 for i in range(1,21)  if i%2==0]
lst3 = [[i for i in range(1,3)] for j in range(3)]
print(lst3)
print(lst)
print(lst1)

=============================DICTIONARY COMPRIHENSION=========================
dct={i:(i**2 if i%2==0 else i**3) for i in range(11)}
dct1={i:i**2 for i in range(11)}
print(dct)
print(dct1)

=============================== SET COMPRIHENSION ==============================
x = [2,4,5,7,8,'pradip',2,4,7,3,5,9,0]
st = {i for i in x}
print(st)
