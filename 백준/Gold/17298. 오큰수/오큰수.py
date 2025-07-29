n = int(input())
numli = list(map(int,input().split()))
stack = []
res = []
for i in range(n-1, -1, -1):
    if not stack:
        res.append(-1)
        stack.append(numli[i])
    else:
        while stack[-1] <= numli[i]:
            stack.pop()
            if not stack:
                break
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
            
        stack.append(numli[i])


for i in range(len(res)):
    print(res.pop(), end=" ")
