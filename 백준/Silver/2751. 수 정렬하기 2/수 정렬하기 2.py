n = int(input())

res = []
for _ in range(n):
    a = int(input())
    res.append(a)
for i in sorted(res):
    print(i)
