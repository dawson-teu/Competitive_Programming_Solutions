t = int(input())

output = []
for i in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())

    total = n
    result = []
    for j in [c, b, a]:
        if total - j < 0:
            result.append(str(total))
            total = 0
        else:
            total -= j
            result.append(str(j))
    if total > 0:
        result = ["-1"]
    result.reverse()
    output.append(result)

for elem in output:
    print(" ".join(elem))
