l, n = map(int, input().split())
arr = list(map(int, input().split()))

result = []

for i in arr:
    if i < n:
        result.append(i)

for i in result:
    print(i, end = " ")