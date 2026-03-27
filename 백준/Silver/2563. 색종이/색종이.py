paper = [[0] * 100 for _ in range(100)]

n = int(input())

for _ in range(n):
    l, b = map(int, input().split())
    for i in range(b, b+10):
        for j in range(l, l+10):
            paper[i][j] = 1

res = 0

for i in paper:
    res += sum(i)

print(res)
