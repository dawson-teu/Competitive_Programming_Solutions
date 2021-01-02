line = input()
a, b, x = [int(line.split(" ")[i]) for i in range(3)]
print((b // x - a // x) + (a % x == 0))
