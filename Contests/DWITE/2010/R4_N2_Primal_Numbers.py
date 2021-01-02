import math


def sieve():
    primes = set()
    for num in range(2, 80918):
        primes.add(num)

    for num in range(2, math.floor(math.sqrt(80918)) + 1):
        if num in primes:
            for j in range(num ** 2, 80918, num):
                if j in primes:
                    primes.remove(j)

    return list(primes)


prime_numbers = sieve()
primal_numbers = []
for i in range(1000):
    primal_numbers.append(prime_numbers[prime_numbers[i] - 1])

output = []
for i in range(5):
    n = int(input())
    output.append(str(primal_numbers[n - 1]))

for elem in output:
    print(elem)
