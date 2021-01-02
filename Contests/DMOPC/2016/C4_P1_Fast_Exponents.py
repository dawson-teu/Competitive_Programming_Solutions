import sys


pow_2 = set()
for i in range(63):
    pow_2.add(2 ** i)

n = int(sys.stdin.readline())
output = []
for i in range(n):
    if int(sys.stdin.readline()) in pow_2:
        output.append("T")
    else:
        output.append("F")

for elem in output:
    print(elem)
