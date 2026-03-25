import math

n, m = list(map(int, input().split()))

for i in range(n, m+1):
    is_num = True
    if i % 2 == 0:
        if i == 2:
            is_num = True
        else:
            is_num = False
    elif i == 1:
        is_num = False
    else:
        for j in range(3, math.ceil(math.sqrt(i))+1):
            if i % j == 0:
                is_num = False
    if is_num:
        print(i)
