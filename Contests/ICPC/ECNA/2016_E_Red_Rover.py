line = input()
min_len = 101
for i in range(len(line)):
    for j in range(i, len(line)):
        new_line = line
        if not i == j:
            new_line = line.replace(line[i:j], "M")
        min_len = min(min_len, len(new_line) + len(line[i:j]))
print(min_len)
