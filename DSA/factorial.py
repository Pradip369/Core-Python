def find_fact(n):

    '''
        > This function is find the factorial of given user input.
        > For ex. 5! = 5 x 4 x 3 x 2 x 1
    '''

    if n == 0:
        c = 1
    else:
        c = n * find_fact(n - 1)
    return c

print(find_fact(5))