N = int(input())
N_li = []
for _ in range(N):
    x, y = map(int, input().split())
    N_li.append([x, y])

res_li = [1] * N
for i in range(N):
    for j in range(N):
        if (N_li[j][0] > N_li[i][0]) and (N_li[j][1] > N_li[i][1]):
            res_li[i] += 1

print(*res_li)