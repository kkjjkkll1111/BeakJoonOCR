n, m = map(int, input().split())

num_list = list(map(int, input().split()))

min_num = m
result = 0
for i in num_list:
    for j in num_list:
        for k in num_list:
            if i != j and i != k and j != k:
                diff = m - (i + j + k)
                if min_num > diff:
                    if i + j + k <= m:
                        min_num = diff
                        result = i + j + k


print(result)