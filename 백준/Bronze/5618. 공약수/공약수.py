n = int(input())
nums = list(map(int, input().split()))

div = min(nums)
res = []
for i in range(1,div+1):
    count = 0
    for num in nums:
        if num % i == 0:
            count += 1
    if count == n:
        res.append(i)

for i in res:
    print(i)
