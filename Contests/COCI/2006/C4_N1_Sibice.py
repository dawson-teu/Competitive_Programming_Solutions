import math

data = input().split(" ")
n = int(data[0])
w = int(data[1])
h = int(data[2])
max_size = math.sqrt(w ** 2 + h ** 2)

output = []
for i in range(n):
    match = int(input())
    if match <= max_size:
        output.append("DA")
    else:
        output.append("NE")

for elem in output:
    print(elem)
