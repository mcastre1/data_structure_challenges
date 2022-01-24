
def anagram(s1, s2):
    """
    This function returns true if both passed in strings are anagrams to each other.
    """

    # Get rid off all white space and capitalization.
    a = s1.lower().replace(" ", "")
    b = s2.lower().replace(" ", "")

    # Convert the above strings into dictionaries
    dict_a = convert_dict(a)
    dict_b = convert_dict(b)

    # If both dictionaries are the same then we know they are anagrams.
    if(dict_a == dict_b):
        return True

    else:
        return False

def convert_dict(str):
    """
    This function retuns a dictionary containing number of occurences of each character
    in the passed in string. 
    """
    temp_dict = {}

    # For each character in string check whethere it is already a key in 
    # the temp dictionary, if not then create the key and assign it the value of 1
    # else increment the value of the character key.
    for c in str:
        if not c in temp_dict.keys():
            temp_dict[c] = 1
        else:
            temp_dict[c] += 1
    
    return temp_dict


print(anagram("clint eastwood","old west action"))