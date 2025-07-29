str_list = []
len_list = []
for i in range(5):
    string = input()
    str_list.append(string)
    len_list.append(len(string))
    
for i in range(max(len_list)):
    for j in range(5):
        if i < len_list[j]:
            print(str_list[j][i], end="")