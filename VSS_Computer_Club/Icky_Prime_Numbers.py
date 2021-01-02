import math

primes = []
for i in range(2, 101):
    is_prime = True
    for j in range(2, math.floor(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        primes.append(i)

n = int(input())
fact = 1
for i in range(1, n + 1):
    if i not in primes:
        fact *= i
print(fact)
