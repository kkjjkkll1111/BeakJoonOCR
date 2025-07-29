def print_star(n):
    if n == 1:
        return '*'
    else:
        new_n = print_star(n//3)

        star = []
        for i in new_n:
            star.append(i*3)
        for i in new_n:
            star.append(i + " "*(n//3) + i)
        for i in new_n:
            star.append(i*3)
        return star
        

n = int(input())

star = print_star(n)
for i in star:
    print(i)