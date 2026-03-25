import sys
s = set()
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    if len(cmd) < 2:
        if cmd[0] == "all":
             s = {i for i in range(1, 21)}
        else:
            s.clear()
    else:
        val = int(cmd[1])
        if cmd[0] == "add":
            s.add(val)
        elif cmd[0] == "check":
            print(int(val in s))
        elif cmd[0] == "toggle":
            if val in s:
                s.discard(val)
            else :
                s.add(val)
        elif cmd[0] == "remove":
            s.discard(val)
