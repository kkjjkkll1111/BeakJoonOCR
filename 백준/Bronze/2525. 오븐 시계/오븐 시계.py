h, m = input().split()
n = int(input())
h = int(h); m = int(m)

nh = n // 60
nm = n % 60
h += nh
m += nm
if(m > 59):
    m -= 60
    h += 1
if(h > 23):
    h -= 24
print(h, m)