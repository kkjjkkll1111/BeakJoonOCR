c_n = int(input())
link = int(input())

graph = [[0] * c_n for _ in range(c_n)]
computers = [0] * c_n
d_stack = []
res = 0

for _ in range(link):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

d_stack.append(0)
computers[0] = 1
while d_stack:
    cpt = d_stack.pop()
    for idx, i in enumerate(graph[cpt]):
        if i != 0 and computers[idx] != 1:
            d_stack.append(idx)
            computers[idx] = 1
            res += 1
print(res)
