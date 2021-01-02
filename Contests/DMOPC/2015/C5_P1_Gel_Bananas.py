import math

a, b, x = [int(input()) for i in range(3)]
print(int((x - 1) // ((a * b) / math.gcd(a, b))) + 1)
