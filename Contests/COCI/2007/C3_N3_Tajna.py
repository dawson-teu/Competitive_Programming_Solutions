import math


def dim(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append([i, n // i])
    return max(factors, key=lambda x: x[0])


string = input()
r, c = dim(len(string))
matrix = [['' for j in range(c)] for i in range(r)]

for i in range(c):
    for j in range(r):
        matrix[j][i] = string[i * r + j]

output = ""
for i in range(r):
    for j in range(c):
        output += matrix[i][j]
print(output)
