line = input()
c, r = [int(line.split(" ")[i]) for i in range(2)]
total = 0
chars = []
for i in range(r):
    line = input()
    for j in range(c):
        if not line[j] == " ":
            total += 1
        if not line[j] in chars and not line[j] in [" ", "."]:
            chars.append(line[j])
print(total + len(chars))
