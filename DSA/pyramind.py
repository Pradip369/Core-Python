# n = 10
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end='')
#     print()

n = 10
k = 20
for i in range(1,n+1):
    print(' '*k,end='')
    print("* "*i)
    k-=1