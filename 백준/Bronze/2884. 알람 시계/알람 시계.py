h, m = input().split()
h = int(h); m = int(m)

if (m - 45 < 0):
    if (h - 1 < 0):
        h = 23
    else:
        h -= 1
    m = m+60 - 45
else:
    m -= 45

print(h, m)