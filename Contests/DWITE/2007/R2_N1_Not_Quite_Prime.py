primes = []
for i in range(2, 1001):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime:
        primes.append(i)

semiprimes = set()
for i in range(len(primes)):
    for j in range(i, len(primes)):
        if primes[i] * primes[j] <= 1000:
            semiprimes.add(primes[i] * primes[j])

output = []
for i in range(5):
    n = int(input())
    if n in semiprimes:
        output.append("semiprime")
    else:
        output.append("not")

for elem in output:
    print(elem)
