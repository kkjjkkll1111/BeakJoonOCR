price = int(input())
item = int(input())
tot = 0
for i in range(item):
    i_reice, i_count = map(int, input().split())
    tot += i_reice * i_count
if tot == price:
    print("Yes")
else:
    print("No")