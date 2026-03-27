from collections import deque
n = int(input())

res = deque([n+1 for n in range(n)])

while len(res) > 1:
    res.popleft()
    res.rotate(-1)

print(res[0])