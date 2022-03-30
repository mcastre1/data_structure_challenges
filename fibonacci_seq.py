def fib_recursively(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        return fib_recursively(n-1) + fib_recursively(n-2)

#print(fib_recursively(35))


nums = {}
def fib_memoization(n):
    global nums
    
    if not n in nums:
        if n in (0,1):
            nums[n] = 1
            return 1
        else:
            n1 = fib_memoization(n-1)
            n2 = fib_memoization(n-2)
            
            if not n1 in nums:
                nums[n-1] = n1
            if not n2 in nums:
                nums[n-2] = n2

            return n1 + n2
    else:
        return nums[n]


#print(fib_memoization(989))



def fib_iter(n):
    a, b = 0, 1

    for i in range(n):
        a,b = b,a+b
    
    return a


print(fib_iter(10))

        
        