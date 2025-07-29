n = int(input())
result = 0
for i in range(n):
    check = True
    word = input()
    ls = []
    for w in range(len(word)):
        if word[w] not in ls:
            ls.append(word[w])
        else:
            if w > 0 and word[w-1] != word[w]:
                check = False
                break

    if check:
        result += 1

print(result)
