n = int(input())

heights = list(map(int, input().split()))
towers = []
for i in range(n):
    towers.append([heights[i], i+1])

stack = []
answer = []
for tower in towers:
    while True:
        if not stack:
            answer.append(0)
            stack.append(tower)
            break
        else:
            if tower[0] > stack[-1][0]:
                stack.pop()
            elif tower[0] <= stack[-1][0]:
                answer.append(stack[-1][1])
                stack.append(tower)
                break
        
    
for a in answer:
    print(a, end = ' ')