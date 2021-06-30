import math
import sys

sieve = [True for i in range(219824)]
sieve[0] = False
sieve[1] = False
for i in range(int(math.sqrt(219824)) + 1):
    if sieve[i]:
        for j in range(i ** 2, 219824, i):
            sieve[j] = False
primes = [0 for i in range(19599)]
cur_index = 0
for j in range(219824):
    if sieve[j]:
        primes[cur_index] = j
        cur_index += 1

primes_index = [0 for i in range(219824)]
cur_prime_index = -1
for j in range(219824):
    if sieve[j]:
        cur_prime_index += 1
    primes_index[j] = cur_prime_index

primes_psa = [0 for i in range(len(primes) + 1)]
for i in range(len(primes)):
    primes_psa[i + 1] = primes_psa[i] + primes[i]

q = int(sys.stdin.readline())
for i in range(q):
    x, k = map(int, sys.stdin.readline().split())
    if sieve[x]:
        x_index = primes_index[x]
    else:
        x_index = primes_index[x] + 1
    print(primes[x_index + k - 1], primes_psa[x_index + k] - primes_psa[x_index])
