import math

n = int(input())

output = []
for i in range(n):
    data = input().split(" ")
    n = int(data[0])
    a = int(data[1])
    b = int(data[2])
    t = int(data[3])

    val = math.ceil((t + b * n) / (a + b))
    if val > n:
        output.append(-1)
    else:
        output.append(val)

for elem in output:
    print(elem)
