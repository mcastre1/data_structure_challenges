import enum
import collections

def finder(arr1, arr2):
    """
    With the help of the sort function we find a missing number from arr2.
    """
    # If both lists have the same length, then we return becasue we need an array 
    # with a missing number.
    if len(arr1) == len(arr2):
        print("Both lists have the same number of items!")
        return
    
    # Prepare both arrays by sorting them.
    arr1.sort()
    arr2.sort()
    arr2.append(-1)

    for i in range(len(arr1)):
        if not arr1[i] == arr2[i]:
            print(f"{arr1[i]} is the missing number!")
            return


def finder_hash(arr1, arr2):
    
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1


finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])
print(finder_hash([1,2,3,4,5,6,7], [3,7,2,1,4,6]))