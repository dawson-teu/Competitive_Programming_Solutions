line = input()
line = line.rstrip(" =")
line = line.split(" ")

total = int(line[0])
for i in range(len(line) - 1):
    if line[i] == "P":
        total += int(line[i + 1])
    elif line[i] == "M":
        total -= int(line[i + 1])
print(total)
