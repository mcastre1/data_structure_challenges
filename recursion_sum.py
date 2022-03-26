def rec_sum(n):
    '''
    Function computes cumulative sum by using recursion.
    '''

    # Base case, we can also make 1 be a base case.
    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1) # Recursion.

# Test, should return 10
print(rec_sum(4))