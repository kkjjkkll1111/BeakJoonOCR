n, m = map(int, input().split())
n_set = set()
m_set = set()
for _ in range(n):
    name = input()
    n_set.add(name)

for _ in range(m):
    name = input()
    m_set.add(name)

res = list(n_set & m_set)

print(len(res))
for r in sorted(res):
    print(r)
