line = input()
a = [int(line.split(" ")[i]) for i in range(3)]
line = input()
b = [int(line.split(" ")[i]) for i in range(3)]
line = input()
c = [int(line.split(" ")[i]) for i in range(3)]

total = 0
for i in range(3):
    if b[i] == a[(i - 1) % 3] and c[i] > 0:
        total += c[i]
print(total)
