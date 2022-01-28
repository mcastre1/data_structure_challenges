def pair_sum(arr, val):
    """
    This function returns a list of tuples.
    Each tuple represent a pair of numbers found in arr that when summed
    together equal val.

    Only unique pairs are returned.
    """
    # Keeps track of all found unique pairs
    pairs = []

    # Iterate through the arr and compare each value with all the other
    for a in arr:
        for b in arr:

            # If a + b equal the given val, check if we have a unique pair
            # If so, then add it to the list.
            if (a + b) == val:
                if not (a,b) in pairs and not (b, a) in pairs:
                    pairs.append((a,b))
            
    return pairs

# Case
print(pair_sum([1,3,2,2], 4))

    
