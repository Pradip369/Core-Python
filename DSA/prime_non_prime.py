def check_prime(n):
    if n % 2 == 0:
        print("This is not prime number")
    else:
        print("This is prime number")
n = 0
while n <= 5:
    user_input = int(input("Enter any no. to check this no.i is prime or not : "))
    check_prime(user_input)
    n+=1