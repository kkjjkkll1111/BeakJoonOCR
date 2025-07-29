is_ppap = True
string = input()
stack = []
for s in string:
    if not stack:
        if s == 'P':
            stack.append(s)
        else:
            is_ppap = False
            break
    else:
        if s == 'P':
            if stack[-1] == 'A':
                stack.pop()
            stack.append(s)
        elif s == 'A':
            if (stack[-1] == 'A') or (stack[-1] == 'P' and len(stack) < 2):
                is_ppap = False
                break
            else:
                stack.pop()
                stack.pop()
                stack.append(s)
        

if is_ppap and stack == ["P"]:
    print("PPAP")
else:
    print("NP")
