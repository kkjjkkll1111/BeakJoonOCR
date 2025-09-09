import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

count = 1
top = li[-1]

for i in reversed(li):
    if top < i:
        count += 1
        top = i
        
print(count)