n,m = map(int, input().split())

arr = [0] * n
for idx in range(m):
    i, j, k = map(int, input().split())
    i -= 1
    for num in range(i,j):
        arr[num] = k

for a in arr:
    print(a, end = " ")