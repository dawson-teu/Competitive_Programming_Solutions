n = int(input())

output = []
for i in range(n):
    line = input()
    new_line = []
    for word in line.split(" "):
        if len(word) == 4:
            new_line.append("****")
        else:
            new_line.append(word)
    output.append(" ".join(new_line))

for line in output:
    print(line)
