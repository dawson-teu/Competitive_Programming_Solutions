import math


def prime_sum_array():
    array = []
    for i in range(2, 100002):
        prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                prime = False
        if prime:
            array.append((0 if len(array) == 0 else array[-1]) + i)
        else:
            array.append(array[-1])
    return array


prime_sum_arr = prime_sum_array()
output = []
for _ in range(5):
    output.append(prime_sum_arr[int(input()) - 2])

for elem in output:
    print(elem)
