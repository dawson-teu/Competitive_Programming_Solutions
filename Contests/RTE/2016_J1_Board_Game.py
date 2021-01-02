line = input()
line = line.replace(" ", "")

total = 0
for i in range(len(line)):
    if line[i] == "L":
        total += 1

count = 0
max_count = -1
for i in range(len(line)):
    if line[i] == "L":
        count += 1
    elif not line[i] == "L" and not i == len(line) - 1 and line[i + 1] == "L":
        max_count = max(max_count, count)
        count = 0
max_count = max(max_count, count)
print(str(total) + " " + str(max_count))
