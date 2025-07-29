string = input()

num = ['1','2','3','4','5','6','7','8','9']
word_value = {'H': 1, 'C': 12, 'O': 16}
stack = []

for i in string:
    if i in word_value.keys():
        stack.append(word_value[i])
    elif i in num:
        stack.append(int(i)*stack.pop())
    elif i == "(":
        stack.append(i)
    elif i == ")":
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                break
            else:
                temp += int(top)
        stack.append(temp)

print(sum(stack))