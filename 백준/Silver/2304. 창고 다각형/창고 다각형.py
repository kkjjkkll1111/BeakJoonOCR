n = int(input())

stack = []
res = 0
inputs = []
cnt = 0
for _ in range(n):
    l, h = map(int, input().split())
    if cnt < l:
        cnt = l
    inputs.append([l, h])

cnt += 1
inputs.sort()

max_h = 0
for l, h in inputs:
    while stack and stack[-1][1] < h and stack[-1][1] < max_h:
        stack.pop()
    
    stack.append([l, h])
    
    if h > max_h:
        max_h = h

for i in range(len(stack) - 1):
    if stack[i + 1][1] < stack[i][1]:
        res += (stack[i + 1][0] - stack[i][0] - 1) * stack[i+1][1] + stack[i][1]
    else:
        res += (stack[i + 1][0] - stack[i][0]) * stack[i][1]

res += (cnt - stack[-1][0]) * stack[-1][1]
print(res)
