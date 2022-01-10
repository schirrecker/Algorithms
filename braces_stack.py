BRACES = { '(': ')', '[': ']', '{': '}' }

def group_check(s):
    stack = []
    for b in s:
        print ("stack:" , stack)
        print (b)
        print ("-------------")
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack

s = "({(})"
print(group_check(s))
