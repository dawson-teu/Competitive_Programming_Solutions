line = input()
x, n = [int(line.split(" ")[i]) for i in range(2)]
print(str(x // n) + " " + str(x % n))
