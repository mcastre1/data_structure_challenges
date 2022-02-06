def string_compression(str):
    """
    Keep a count of all repeated characters in string
    Return unique char value and how many times it was repeated.
    """
    comp_dict = {}

    # If the given string has length 0, then it is not a valid string
    if len(str) == 0:
        return "Wrong input"

    # Increment each character key in dict. by one
    for c in str:
        if c in comp_dict:
            comp_dict[c] += 1
        else:
            comp_dict[c] = 1

    # Keep track of the output string
    temp_str = ""

    # Add to output string key, value pairs.
    for i in comp_dict:
        temp_str += f"{i}{comp_dict[i]}"

    return temp_str

print(string_compression("AABBCC"))
print(string_compression(""))
print(string_compression("AAAaaa"))
print(string_compression("AAABCCDDDDD"))