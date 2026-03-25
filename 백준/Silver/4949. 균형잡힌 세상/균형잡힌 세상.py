brackets = {')': '(', ']': '['}

while True:
    stack = []
    yn = True
    s = input()
    if s == '.':
        break
    
    for k in s:
        if k in brackets.values():
            stack.append(k)
        elif k in brackets.keys():
            if not stack or stack[-1] != brackets[k]:
                yn = False
            else:
                stack.pop()
    
    if yn and not stack:
        print("yes")
    else:
        print("no")
