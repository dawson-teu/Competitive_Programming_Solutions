import math
import sys


def sieve():
    primes = [False, False]
    for i in range(2, 999999):
        primes.append(True)

    for i in range(2, math.floor(math.sqrt(999999)) + 1):
        if primes[i]:
            for j in range(i ** 2, 999999, i):
                if primes[j]:
                    primes[j] = False
    return primes


n = int(input())

# output = []
prime_nums = sieve()
for _ in range(n):
    data = sys.stdin.readline().split(" ")
    num1 = int(data[0])
    num2 = int(data[1])
    print(len([i for i in prime_nums[num1:num2] if i]))
    # output.append(sieve(num1, num2))

# for elem in output:
#     print(elem)
