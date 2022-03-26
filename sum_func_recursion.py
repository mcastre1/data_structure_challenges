def sum_func(n):
    '''
    Fucntion recursively splits n into single digits and adds them together 
    '''
    # Base case, if there is only 1 digit left, return n.
    if n//10 == 0:
        return n
    else:
        return (n % 10) + sum_func(n//10) # Recursion call


# Test, should return 10
print(sum_func(4321))