import math

primes = set()
for i in range(2, 1001):
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        primes.add(i)

output = []
for _ in range(5):
    n = int(input())
    total = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and i in primes:
            total += 1
            if n % (n // i) == 0 and (n // i) in primes:
                total += 1

    if total == 3:
        output.append("valid")
    else:
        output.append("not")

for elem in output:
    print(elem)
