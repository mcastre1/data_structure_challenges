reversed_string = ""

def reverse(s):
    '''
    Reversing a given string s, with recursion.
    '''
    global reversed_string # Makes use of global keyword to keep track of reversed string.
    
    # Base case
    if len(s) == 0:
        return reversed_string
    
    # Save the last character in the string in the reversed_string variable.
    reversed_string = f"{reversed_string}{s[-1]}"

    # Recursion
    return reverse(s[:-1])

print(reverse("hello my beautiful leecia!"))