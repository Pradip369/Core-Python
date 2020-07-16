def outer(fun):
    def inner():
        value=fun()
        print(1,value)
        return value*5
    return inner
def outer1(fun):
    def inner():
        value=fun()
        print(2,value)
        return value+5
    return inner
@outer
@outer1
def num():
    return 3
print(num())
        
    