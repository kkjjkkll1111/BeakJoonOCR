n, d = map(int, input().split())
res = 0

for i in range(1,n+1):
    while i > 0:
        num = i % 10
        if num == d:
            res += 1
        i //= 10
print(res)