import math

big_num = 600851475143

largest_factor = -1
while big_num % 2 == 0:
    big_num //= 2
    largest_factor = max(largest_factor, 2)

for i in range(3, math.floor(math.sqrt(big_num)), 2):
    while big_num % i == 0:
        big_num //= i
        largest_factor = max(largest_factor, i)
print(largest_factor)
