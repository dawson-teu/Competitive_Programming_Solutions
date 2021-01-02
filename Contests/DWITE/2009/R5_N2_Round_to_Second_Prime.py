def primes():
    result = set()
    for num in range(2, 104):
        prime = True
        for num2 in range(2, num):
            if num % num2 == 0:
                prime = False
        if prime:
            result.add(num)
    return result


prime_num = primes()

output = []
for i in range(5):
    n = int(input())

    high_prime = 0
    count = 0
    for j in range(n + 1, 104):
        if j in prime_num and count == 1:
            high_prime = j
            break
        elif j in prime_num:
            count += 1

    low_prime = 0
    count = 0
    for j in range(n - 1, 1, -1):
        if j in prime_num and count == 1:
            low_prime = j
            break
        elif j in prime_num:
            count += 1

    if abs(high_prime - n) < abs(low_prime - n):
        output.append(high_prime)
    elif abs(low_prime - n) < abs(high_prime - n):
        output.append(low_prime)
    else:
        output.append(high_prime)

for elem in output:
    print(elem)
