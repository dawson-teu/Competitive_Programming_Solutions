n = int(input())

output = []
for i in range(n):
    line = input() + " "
    compress = []
    count = 0
    for j in range(1, len(line)):
        if line[j] == line[j - 1]:
            count += 1
        elif not line[j] == line[j - 1]:
            compress.append([line[j - 1], count + 1])
            count = 0
    output.append(compress)

for elem in output:
    compressed = []
    for pair in elem:
        compressed.append(str(pair[1]) + " " + pair[0])
    print(" ".join(compressed))
