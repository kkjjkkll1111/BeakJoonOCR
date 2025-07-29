while(1):
    instr = input()
    num = 0
    if (instr == "#"):
        break
    for i in instr:
        if(i.lower() in ['a', 'e', 'u', 'i', 'o']):
            num += 1
    print(num)


