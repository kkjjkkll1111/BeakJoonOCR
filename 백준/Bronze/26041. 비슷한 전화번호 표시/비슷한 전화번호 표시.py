str_list = input().split()
head = input()
res = []

for sl in str_list:
    if len(sl) > len(head):
        if sl[:len(head)] == head:
            res.append(sl)

print(len(res))
