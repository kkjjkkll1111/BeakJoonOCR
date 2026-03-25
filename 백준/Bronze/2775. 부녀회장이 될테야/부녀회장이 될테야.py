T = int(input())
dp = [[0]*15 for _ in range(15)]
res = []

for i in range(1, 15):
    dp[0][i] = i

for a in range(1, 15):
    for b in range(1, 15):
        dp[a][b] = dp[a-1][b] + dp[a][b-1]
        
for _ in range(T):
    k = int(input())
    n = int(input())
    res.append(dp[k][n])

for num in res:
    print(num)