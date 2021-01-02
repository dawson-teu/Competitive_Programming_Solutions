d = int(input())
output = []
for n in range(d):
    t = int(input())
    total = sum([int(input()) for i in range(t)])
    if total == 0:
        output.append("Weekend")
    else:
        output.append("Day " + str(n + 1) + ": " + str(total))

for line in output:
    print(line)
