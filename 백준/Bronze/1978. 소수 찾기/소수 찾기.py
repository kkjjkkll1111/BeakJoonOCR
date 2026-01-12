import math
n = int(input())
cnt = 0
nums = list(map(int, input().split()))
for m in nums:
    is_num = True
    if m % 2 == 0:
        if m == 2:
            is_num = True
        else:
            is_num = False
    elif m == 1:
        is_num = False
    else:
        for i in range(3, math.ceil(math.sqrt(m))+1):
            if m % i == 0:
                is_num = False
    if is_num:
        cnt += 1
print(cnt)