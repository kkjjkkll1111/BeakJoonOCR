res = 0
for i in range(3, 0, -1):
    s = input()
    if s not in ["Fizz","Buzz","FizzBuzz"]:
        res = int(s) + i

if res % 3 == 0 and res % 5 == 0:
    print("FizzBuzz")
elif res % 3 == 0 and res % 5 != 0:
    print("Fizz")
elif res % 3 != 0 and res % 5 == 0:
    print("Buzz")
else:
    print(res)
