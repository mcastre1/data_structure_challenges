def cuboid_sum(x, y, z, n):
    """
    List comprehension exercise from hackerrank.
    Return a list of all x, y, z combination that do not sum up to n
    """
    out_list = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if not i + j + k == n:
                    out_list.append([i, j, k])


    return out_list


print(cuboid_sum(1,1,1,2))