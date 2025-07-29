string = input()
stack = []
result = 0
for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
    elif string[i] == ')':
        stack.pop()
        if string[i - 1] == '(':
            result += len(stack)
        elif string[i - 1] == ')':
            result += 1

print(result)