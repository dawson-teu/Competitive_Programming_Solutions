data = input().split(" ")
n = int(data[0])
k = int(data[1])

primes = set()
for num in range(2, n + 1):
    primes.add(num)

count = 0
for num in range(2, n + 1):
    if num in primes:
        for j in range(num, n + 1, num):
            if j in primes:
                primes.remove(j)
                count += 1
            if count == k:
                print(j)
                break
