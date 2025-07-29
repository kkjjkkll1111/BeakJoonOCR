n = int(input())
count = 1

while n > 0:
    if n == 1:
        break
    n -= count * 6
    count += 1
    

print(count)
