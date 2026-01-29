n = int(input())
li = []
for _ in range(n):
    num_li = list(map(int, input().split()))
    li.append(num_li)
li.sort()

for i, j in li:
    print(i, j)