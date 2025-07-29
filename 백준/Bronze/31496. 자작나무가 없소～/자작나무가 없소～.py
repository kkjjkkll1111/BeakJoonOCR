n, s = input().split()
tot = 0

for i in range(int(n)):
    a, b = input().split()

    sa = list(a.split("_"))

    for j in sa:
        if j == s:
            tot += int(b)
            break


print(tot)