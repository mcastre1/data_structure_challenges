def balance_check(str):
    '''Method used to check whther a give string is a balanced parentheses.
    '''
    s = [] # Stack representation
    
    # Try to add and remove from stack.
    try:
        for c in str:
            if c == '[':
                s.append(']')
            elif c == '(':
                s.append(')')
            elif c == '{':
                s.append('}')
            elif c == ')':
                s.remove(')')
            elif c == '}':
                s.remove('}')
            elif c == ']':
                s.remove(']')
    except:
        return False

    if s == []:
        return True
    else:
        return False


print(balance_check("[]"))
print(balance_check("[](){([[[]]])}"))
print(balance_check("()(){]}"))


