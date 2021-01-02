import math


def sieve():
    primes = [False, False]
    for k in range(2, 10001):
        primes.append(True)

    for k in range(2, math.floor(math.sqrt(10001)) + 1):
        if primes[k]:
            for m in range(k ** 2, 10001, k):
                if primes[m]:
                    primes[m] = False
    return [k for k in range(len(primes)) if primes[k]]


p = sieve()
result = []
for i in range(5):
    n = int(input())
    factorization = []
    for prime in p:
        if n // prime == 0:
            break
        total = 0
        for j in range(1, 14):
            if n // (prime ** i) == 0:
                break
            else:
                total += n // (prime ** j)
        factorization.append([prime, total])

    output = str(factorization[0][0]) + "^" + str(factorization[0][1])
    for factor in factorization[1:]:
        output += " * " + str(factor[0]) + "^" + str(factor[1])
    result.append(output)

for elem in result:
    print(elem)
