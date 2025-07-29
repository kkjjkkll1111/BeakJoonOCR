word = input()
word_list = []
for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        a = "".join(reversed(list(word[:i])))
        b = "".join(reversed(list(word[i:j])))
        c = "".join(reversed(list(word[j:])))
        result = a + b + c
        word_list.append(result)

print(sorted(word_list)[0])