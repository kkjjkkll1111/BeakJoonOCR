n = int(input())

people_time = list(map(int, input().split()))

res = 0
tot = 0
for i in sorted(people_time):
    tot += i
    res += tot
print(res)