def uni_char(s):
    # Dictionary keeps track of all seen characters in the given string.
    cdir = {}

    # Iterate through all characters in string.
    for c in s:
        # If the character is found in the temporary dictionary, we return false.
        # Else we just add it to our temporary dictionary.
        if c in cdir:
            return False
        else:
            cdir[c] = 1

    # If no character was found in the above loop, then we always return True.
    return True