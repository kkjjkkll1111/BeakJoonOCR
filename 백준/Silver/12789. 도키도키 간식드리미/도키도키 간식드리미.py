n = int(input())
li = list(map(int, input().split()))
now = 1
stack = []
i = 0
while i < len(li):
    if li[i] == now:
        now += 1
        i += 1
    elif li[i] != now:
            if stack and stack[-1] == now:
                stack.pop()
                now += 1
            else:
                stack.append(li[i])
                i += 1
    
for _ in range(len(stack)):
    if stack[-1] == now:
        stack.pop()
        now += 1
        
if not stack:
    print("Nice")
else:
    print("Sad")