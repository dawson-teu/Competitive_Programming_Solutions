n = int(input())
t = 0
s = 0
for i in range(n):
    line = input()
    for char in line:
        if char.lower() == "t":
            t += 1
        elif char.lower() == "s":
            s += 1

if t > s:
    print("English")
else:
    print("French")
