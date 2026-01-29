n, k = map(int, input().split())

li = [num for num in range(1,n+1)]
cnt = 0
res = []
while True:
    h = li.pop(0)
    cnt += 1
    if cnt != k:
        li.append(h)
    else:
        cnt = 0
        res.append(str(h))
    if not li:
        break

print("<" + ", ".join(res) + ">")