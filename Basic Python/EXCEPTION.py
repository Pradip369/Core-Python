
==================================ASSERT===============================================
k=int(input("enter number"))
assert k>30,"you are wrong"
print('right')
===============================================================================================
==============================>TRY AND EXCEPT-------RAISE<=======================================
================================================================================================
class myexception(Exception):
    def __init__(self,msg):
        self.msg=msg
while True:
    o=input("Enter Your Name ")
    try:
        if o=="" or len(o)<=1:
            raise myexception(" Please Enter Your Name")
        else:
            print(f"welcome {o}")
            break
       
    except myexception as me:
        print(me)
