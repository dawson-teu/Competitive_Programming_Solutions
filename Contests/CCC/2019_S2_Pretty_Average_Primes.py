import sys
import math


t = int(sys.stdin.readline())

output = []
prime_num = {}
for k in range(t):
    n = int(sys.stdin.readline())
    for i in range(2, n + 1):
        a = i
        b = 2 * n - i

        if a in prime_num:
            a_prime = prime_num[a]
        else:
            a_prime = True
            for j in range(2, math.ceil(math.sqrt(a)) + 1):
                if a % j == 0:
                    a_prime = False
                    break
            prime_num[a] = a_prime

        if b in prime_num:
            b_prime = prime_num[b]
        else:
            b_prime = True
            for j in range(2, math.ceil(math.sqrt(b)) + 1):
                if b % j == 0:
                    b_prime = False
                    break
            prime_num[b] = b_prime

        if a_prime and b_prime:
            output.append(str(a) + " " + str(b))
            break

for elem in output:
    print(elem)
