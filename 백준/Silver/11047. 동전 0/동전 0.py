num, money = map(int, input().split())

m_type = []
for _ in range(num):
    m = int(input())
    m_type.append(m)

res = 0
for m in m_type[::-1]:
    while money >= m:
        money -= m
        res += 1

print(res)