n, m = map(int, input().split())
li = []
for i in range(n):
    li.append(i+1)
    
for j in range(m):
    a, b = map(int, input().split())
    temp = 0
    temp = li[a-1]
    li[a-1] = li[b-1]
    li[b-1] = temp

for i in li:
    print(i, end = " ")