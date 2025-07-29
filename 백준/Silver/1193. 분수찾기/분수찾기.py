n = int(input())

line = 1

while n > line:
    n -= line
    line += 1

if (line % 2) == 0:
    start = n
    end = line - n + 1
else:
    start = line - n + 1
    end = n

print(str(start)+"/"+str(end))

