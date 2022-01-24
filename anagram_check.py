import collections
from lib2to3.pytree import convert


def anagram(s1, s2):
    a = s1.lower().replace(" ", "")
    b = s2.lower().replace(" ", "")

    dict_a = convert_dict(a)
    dict_b = convert_dict(b)

    if(dict_a == dict_b):
        return True

    else:
        return False

def convert_dict(str):
    temp_dict = {}

    for c in str:
        if not c in temp_dict.keys():
            temp_dict[c] = 1
        else:
            temp_dict[c] += 1
    
    return temp_dict


print(anagram("clint eastwood","old west action"))