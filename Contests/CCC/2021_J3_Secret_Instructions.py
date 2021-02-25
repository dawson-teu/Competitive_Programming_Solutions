line = input()
output = []
while not line == "99999":
    if (int(line[0]) + int(line[1])) == 0:
        output.append((output[-1][0], line[2:]))
    elif (int(line[0]) + int(line[1])) % 2 == 1:
        output.append(("left", line[2:]))
    elif (int(line[0]) + int(line[1])) % 2 == 0:
        output.append(("right", line[2:]))
    line = input()
for elem in output:
    print(elem[0] + " " + elem[1])
