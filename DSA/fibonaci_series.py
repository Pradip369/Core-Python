# def fibonacci_seq(n):
#     a = 0
#     b = 1

#     fib_lst = [a]

#     if n == 0:
#         return fib_lst
#     elif n == 1:
#         fib_lst.append(b)
#     else:
#         fib_lst.append(b)
#         for i in range(n-2):
#             c = a + b
#             a = b
#             b = c
#             fib_lst.append(b)
#     return fib_lst

# user_input = int(input("Enter no. of fibonacci sequesnce range : "))
# print(fibonacci_seq(user_input))

# def fibo(n):
#     a = 0
#     b = 1
#     count = 0

#     if n == 0:
#         print(0)
    
#     elif n == 1:
#         print(b)

#     else:
#         while count < n:
#             if b > n:
#                 break
#             else:
#                 print(b)
#                 c = a + b
#                 a = b
#                 b = c
#                 count += 1

# fibo(20)