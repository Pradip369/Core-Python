# ==================================Generator===========================
def gen():
    yield 'a'
    yield 'b'
    yield 'c'
def nor():
    print("a")
    print("b")
    print("c")
# g=gen()
n=nor()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# ===============================MODULE===========================================
def add(s,d):
    '''this is a doc string'''
    print(add.__doc__)
    print(__name__)
    print(s+d)
def num(a):
    print(a*3)
if __name__=="__main__":
    add(3,4)
    print("main file")
else:
    print("module file")