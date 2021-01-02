import math

p = int(input())
n = int(input())
r = int(input())

if r == 1:
    print(p // n)
else:
    print(math.floor(math.log(1 - (p * (1 - r)) / n, r)))
