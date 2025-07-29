hot = int(input())

stage = 1
result = 0
while hot > 0:
    result += (hot % 7) * stage
    hot //= 7
    stage *= 3

print(result)