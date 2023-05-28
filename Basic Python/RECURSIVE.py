# ==============================RECURSIVE FUNCTION==================
def fectorial(n):
    if n==0:
        result=1
    else:
        result=n*fectorial(n-1)
    return result
for x in range(1,20):
    print(f"fectorial of {x} is {fectorial(x)}")       
# ===================================MODULE=======================        
from GENERATOR import *
f = add(2,5)
g = num(6)
# print(__name__)
print(__file__)
print(add.__name__)