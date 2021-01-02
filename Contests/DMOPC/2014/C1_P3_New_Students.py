init = int(input())
total = 0
for i in range(init):
    total += int(input())

s = int(input())
output = []
for i in range(s):
    total += int(input())
    output.append(round(total / (init + i + 1), 3))

for elem in output:
    print(elem)
