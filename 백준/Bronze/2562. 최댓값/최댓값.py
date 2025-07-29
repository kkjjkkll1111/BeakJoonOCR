result = []

for i in range(9):
    n = int(input())
    result.append(n)

print(max(result))
print(result.index(max(result)) + 1)