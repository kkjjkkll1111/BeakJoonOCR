n, m = map(int, input().split())

arr = [i for i in range(1,n+1)]

for c in range(m):
    i, j = map(int, input().split())
    arr = arr[:i-1] + list(reversed(arr[i-1:j])) + arr[j:]

print(*arr)