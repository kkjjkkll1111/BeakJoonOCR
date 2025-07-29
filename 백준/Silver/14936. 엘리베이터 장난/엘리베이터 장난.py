n, m = map(int, input().split())
res = 1

p1 = n
p2 = n // 2
p3 = (n + 1) // 2
p4 = (n - 1) // 3 + 1

if p1 <= m:
    res += 1
if n > 1 and p2 <= m:
    res += 1
if n > 1 and p3 <= m:
    res += 1
if n > 2 and p4 <= m:
    res += 1
if n > 2 and p4 + p1 <= m:
    res += 1
if n > 2 and p4 + p2 <= m:
    res += 1
if n > 2 and p4 + p3 <= m:
    res += 1

print(res)