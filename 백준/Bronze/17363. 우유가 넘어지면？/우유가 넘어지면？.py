n, m = map(int, input().split())

result = []

for i in range(n):
    l1 = list(input())
    arr = []
    for j in l1:
        if j in [".","O"]:
            arr.append(j)
        elif j == "-":
            arr.append('|')
        elif j == "|":
            arr.append('-')
        elif j == "/":
            arr.append('\\')
        elif j == "\\":
            arr.append('/')
        elif j == "^":
            arr.append('<')
        elif j == '<':
            arr.append('v')
        elif j == 'v':
            arr.append('>')
        elif j == '>':
            arr.append('^')
    result.append(arr)

for i in range(m-1, -1, -1):
    for j in range(n):
        print(result[j][i], end="")
    print()
