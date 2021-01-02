line = input()
[n, c] = [int(line.split(" ")[i]) for i in range(2)]

output = []
for i in range(n):
    person = input()
    [name, score] = [person.split(" ")[i] for i in range(2)]
    if int(score) > c:
        output.append(name + " will advance")
    else:
        output.append(name + " will not advance")

for elem in output:
    print(elem)
