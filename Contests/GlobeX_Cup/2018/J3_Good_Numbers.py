import math


def is_prime(num):
    if num <= 1:
        return False
    for j in range(2, int(math.sqrt(num)) + 1):
        if num % j == 0:
            return False
    return True


def is_good(num):
    return is_prime(sum([int(str(num)[j]) for j in range(len(str(num)))])) and is_prime(num)


n = int(input())
total = 0
for i in range(n):
    if is_good(int(input())):
        total += 1
print(total)
