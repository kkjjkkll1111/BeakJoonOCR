n = int(input())
result = ""
for i in range(n):
    a = input()
    list_a = [int(i) for i in a.split()]

    list_a.remove(max(list_a))
    list_a.remove(min(list_a))

    if(max(list_a) - min(list_a) >= 4):
        result = "KIN"
    else:
        result = sum(list_a)
    print(result)
