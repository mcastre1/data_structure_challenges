import enum


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



finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])