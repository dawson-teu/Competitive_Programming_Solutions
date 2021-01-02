import math


def divisors(n):
    output = set()
    for j in range(1, int(math.sqrt(n)) + 1):
        if n % j == 0:
            output.add(j)
            output.add(n // j)
    return output


low = int(input())
high = int(input())
count = 0
for i in range(low, high+1):
    if len(divisors(i)) == 4:
        count += 1
print("The number of RSA numbers between " + str(low) + " and " + str(high) + " is " + str(count))
