from collections import deque

gears = []
for i in range(4):
    gear = deque(list(map(int, list(input()))))
    gears.append(gear)

n = int(input())

for i in range(n):
    num, dire = map(int, input().split())
    num -= 1

    current = []
    for i in gears:
            current.append([i[6], i[2]]) # 2 = right, 6 = left

    if(num != 0): #left gear rotate
        for k in range(num-1, -1, -1):
            if current[k+1][0] != current[k][1]:
                if ((num - k) % 2) == 1:
                    gears[k].rotate(-1 * dire)
                else:
                    gears[k].rotate(dire)
            else:
                break

    if(num != 3): #right gear rotate
        for k in range(num+1, 4):
            if current[k-1][1] != current[k][0]:
                if ((k - num) % 2) == 1:
                    gears[k].rotate(-1 * dire)
                else:
                    gears[k].rotate(dire)
            else:
                break
            
    gears[num].rotate(dire)
      
print((gears[0][0]) + (gears[1][0]*2) + (gears[2][0]*4) + (gears[3][0]*8))