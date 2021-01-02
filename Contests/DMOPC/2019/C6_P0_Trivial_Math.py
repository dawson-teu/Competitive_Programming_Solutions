line = input()
a, b, c = [int(line.split(" ")[i]) for i in range(3)]
if a + b > c and b + c > a and a + c > b:
    print("yes")
else:
    print("no")
