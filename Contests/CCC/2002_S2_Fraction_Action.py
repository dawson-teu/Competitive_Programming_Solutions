import math

a = int(input())
b = int(input())

output = ''
if a // b > 0 or a == 0:
    output += str(a // b) + ' '
    a = a % b
if a > 0:
    output += str(a // math.gcd(a, b)) + '/' + str(b // math.gcd(a, b))
print(output)
