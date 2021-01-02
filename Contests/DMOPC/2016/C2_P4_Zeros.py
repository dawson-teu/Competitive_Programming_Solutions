import math


def trailing_zeros(num):
    total = 0
    for i in range(1, int(math.log(num, 5) + 1)):
        total += num // (5 ** i)
    return total


line = input()
a, b = [int(line.split(" ")[i]) for i in range(2)]

left = 1
right = 10 ** 15 + 1
min_a = 0
while left <= right:
    middle = (left + right) // 2
    middle_val = trailing_zeros(middle)
    if middle_val >= a:
        right = middle - 1
        min_a = middle
    else:
        left = middle + 1

left = 1
right = 10 ** 15 + 1
max_b = 0
while left <= right:
    middle = (left + right) // 2
    middle_val = trailing_zeros(middle)
    if middle_val <= b:
        left = middle + 1
        max_b = middle
    else:
        right = middle - 1
print(max_b - min_a + 1)
