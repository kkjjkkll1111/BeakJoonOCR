import math

n = input()
res = {"0":0,
       "1":0,
       "2":0,
       "3":0,
       "4":0,
       "5":0,
       "7":0,
       "8":0,
       "9":0
       }

for i in n:
    if i == "6":
        res["9"] += 1
    else:
        res[i] += 1

res["9"] = math.ceil(res["9"] / 2)
print(max(res.values()))
    
