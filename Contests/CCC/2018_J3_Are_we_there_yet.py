def dist(a, b):
    total = 0
    for i in range(a, b):
        total += num[i]
    return total


line = input()
num = [int(line.split(" ")[i]) for i in range(4)]

output = []
for i in range(5):
    row = []
    for j in range(5):
        if i == j:
            row.append(0)
        else:
            row.append(dist(min(i, j), max(i, j)))
    output.append(row)

for row in output:
    print(" ".join([str(i) for i in row]))
