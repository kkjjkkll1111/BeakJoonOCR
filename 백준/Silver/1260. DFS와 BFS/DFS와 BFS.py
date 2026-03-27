from collections import deque

n, m, v = map(int, input().split())
n += 1
graph = [[0] * n for _ in range(n)]
dfs = []
bfs = deque([v])
res = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs.append(v)
res.append(v)
while dfs:
    is_all_visited = True
    start = dfs[-1]
    for idx, i in enumerate(graph[start]):
        if i != 0 and idx not in res:
            is_all_visited = False
            dfs.append(idx)
            res.append(idx)
            break
    if is_all_visited:
        dfs.pop()
    
print(*res)

res = [v]
while bfs:
    val = bfs.popleft()
    for idx, i in enumerate(graph[val]):
        if i != 0 and idx not in res:
            bfs.append(idx)
            res.append(idx)
print(*res)