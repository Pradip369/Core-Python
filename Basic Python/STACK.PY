import sys
s = []
choice=0
while choice<5:
    print("STACK OPERATION")
    print("push------1")
    print("pop-------2")
    print("peep------3")
    print("search----4")
    print("exit------5")
    choice+=1
    d=int(input("Enter your opration : "))
    if d==5:
        sys.exit()
    elif d==1:
        elm=input("Add Element : ") 
        s.append(elm)
    elif d==2:
        try:
            elm=s.pop() 
            print('Poped element : ',elm)
        except IndexError:
            print("List is empty")        
    elif d==3:
        try:
            elm=s[-1]
            print('Top most element : ',elm)
        except IndexError:
            print("Empty list")    
    elif d==4:
        elm=input("Enter your searching element : ")
        if elm in s:
            print("Your element position is : ",s.index(elm))
        else:
            print("You enter wrong element or may be list is empty" ) 
    else:
        print("something went wrong")
        break
    print("Your stack is : ",s)