def check_letter(string):
    for i in string:
        if i in keyword.keys():
            keyword[i] += 1
def rate(love):
    l = love[0]; o = love[1]; v = love[2]; e = love[3]
    return ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e)) % 100

engName = input().upper()
n = int(input())
tname_dict = {}
max_rate = 0
for i in range(n):
    keyword = {'L': 0, 'O': 0, 'V': 0, 'E': 0}
    tname = input().upper()
    check_letter(engName)
    check_letter(tname)
    result = rate(list(keyword.values()))
    max_rate = max(max_rate,result)
    tname_dict[tname] = result

max_rate_tname = [j for j in tname_dict.keys() if tname_dict[j] == max_rate]
print(sorted(max_rate_tname)[0])