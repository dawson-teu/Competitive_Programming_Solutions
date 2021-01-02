import math


def sieve():
    primes = [False, False]
    for j in range(2, 7001):
        primes.append(True)

    for j in range(2, math.floor(math.sqrt(7001)) + 1):
        if primes[j]:
            for m in range(j ** 2, 7001, j):
                if primes[m]:
                    primes[m] = False
    return primes


def j_num(num):
    if num < 2:
        return 0
    if prime[num]:
        return 1
    elif num % 2 == 0:
        return 2
    elif prime[num - 2]:
        return 2
    else:
        return 3


line = input()
n, k = [int(line.split(" ")[i]) for i in range(2)]

prime = sieve()
count = 0
for i in range(1, n + 1):
    if j_num(i) == k:
        count += 1
print(count)
