line = input()
a, b = [int(line.split(" ")[i]) for i in range(2)]
line = input()
c, d = [int(line.split(" ")[i]) for i in range(2)]
t = int(input())

dist = abs(d - b) + abs(c - a)
print("Y" if (t - dist) >= 0 and (t - dist) % 2 == 0 else "N")
