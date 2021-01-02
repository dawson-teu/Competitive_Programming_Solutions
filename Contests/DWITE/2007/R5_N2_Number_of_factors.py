def primes():
    result = set()
    for candidate in range(2, 32):
        prime = True
        for j in range(2, candidate):
            if candidate % j == 0:
                prime = False
        if prime:
            result.add(candidate)
    return result


prime_list = primes()

output = []
for i in range(5):
    n = int(input())

    if n in prime_list:
        output.append("0")
    else:
        total = 0
        while n > 1:
            for prime_num in prime_list:
                if n % prime_num == 0:
                    n /= prime_num
                    total += 1
        output.append(str(total))

for elem in output:
    print(elem)
