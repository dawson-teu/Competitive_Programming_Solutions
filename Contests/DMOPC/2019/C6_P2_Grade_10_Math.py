import math


def prime_factorization(n):
    prime_factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        prime_factor = [-1, 0]
        if n % i == 0:
            prime_factor[0] = i
        while n % i == 0:
            n /= i
            prime_factor[1] += 1
        if not prime_factor == [-1, 0]:
            prime_factors.append(prime_factor)
    if not n == 1:
        prime_factors.append([n, 1])
    return prime_factors


line = input()
a, b = [int(line.split(" ")[i]) for i in range(2)]

ans = 10 ** 6 + 1
for factor in prime_factorization(a):
    total = 0
    value = factor[0]
    while not b // value == 0:
        total += b // value
        value *= factor[0]
    ans = min(ans, total // factor[1])
print(int(ans))
