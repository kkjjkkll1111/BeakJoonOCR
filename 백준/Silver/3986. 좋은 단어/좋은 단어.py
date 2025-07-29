n = int(input())
count = 0

for _ in range(n):
    stack = []
    good_word = input()
    for w in good_word:
        if w == 'A' or w == 'B':
            if not stack or stack[-1] != w:
                stack.append(w)
            else:
                stack.pop()
                    
    if stack == []:
        count += 1

print(count)