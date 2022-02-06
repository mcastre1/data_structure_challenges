def largest_cont_sum(nums):
    """
    Find largest continous sum in given array.
    Return the largest cont. sum
    """
    first_pos = 0 
    sums = {}

    # Find the first positive number
    for i, val in enumerate(nums):
        if val > 0:
            first_pos = i
            break

    ind = first_pos
    sum = 0

    # Sum up values and keep track of it by adding to dictionary
    while ind < len(nums):
        sum += nums[ind]
        sums[ind] = sum
        ind += 1

    return sums[max(sums, key= sums.get)]

print(largest_cont_sum([1,2,-1,3,4,-1]))
print(largest_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
print(largest_cont_sum([-1,1]))