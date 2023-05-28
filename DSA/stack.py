import sys

class Stack(object):

    def __init__(self):
        self.lst = []

    def push(self,n):
        self.lst.append(n)

    def pop(self):
        if self.lst:
            self.lst.pop()
        else:
            print("List is empty...")
    
    def show(self):
        print("Your stack is :",self.lst)
        print("----------------------------------------------------")

    def exit(self):
        sys.exit()

stk = Stack()
while True:
    print("Push ------ 1\n","Pop ------ 2 \n","Show ------ 3 \n","Exit ------ 4\n")
    n = int(input("Choose above any one option to perform task : "))
    print("----------------------------------------------------")

    if n == 1:
        ps_no = int(input("Enter number : "))
        stk.push(ps_no)
    elif n == 2:
        stk.pop()
    elif n == 4:
        stk.exit()
    stk.show()