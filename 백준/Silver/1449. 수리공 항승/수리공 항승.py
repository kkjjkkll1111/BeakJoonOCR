n, m = map(int, input().split())
li = list(sorted(map(int, input().split())))
count = 0
start = li[0]

end = start + (m - 1)

for i in range(len(li)):
    if end < li[i]:
        start = li[i]
        end = start + (m - 1)
        count += 1
        continue

if li[-1] <= end:
    count += 1

print(count)