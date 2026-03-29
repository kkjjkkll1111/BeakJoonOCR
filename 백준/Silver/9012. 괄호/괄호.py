t = int(input())

for _ in range(t):
    vps = input()
    stack = []
    is_vps = True
    
    for v in vps:
        if v == "(":
            stack.append(v)
        elif v == ")":
            if not stack:
                is_vps = False
                break
            else:
                stack.pop()
    if stack:
        is_vps = False
    
    if is_vps:
        print("YES")
    else:
        print("NO")
