import math


def is_prime(a):
    prime = True
    for num in range(2, int(math.sqrt(a) + 1)):
        if a % num == 0:
            prime = False
            break
    return prime


n = int(input())
total = 0
for i in range(n):
    if not is_prime(int(input())):
        total += 1
print(total)
