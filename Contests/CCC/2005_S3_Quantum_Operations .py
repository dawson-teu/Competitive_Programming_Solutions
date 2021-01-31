import sys


def tensor_product(a, b):
    m = len(a)
    n = len(a[0])
    p = len(b)
    q = len(b[0])
    matrix = [[0 for _ in range(n * q)] for _ in range(m * p)]

    for i in range(m * p):
        for j in range(n * q):
            matrix[i][j] = a[i // p][j // q] * b[i % p][j % q]
    return matrix


def deep_copy(arr):
    output = []
    for i in range(len(arr)):
        out_row = []
        for j in range(len(arr[0])):
            out_row.append(arr[i][j])
        output.append(out_row)
    return output


def flatten(arr):
    flat = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            flat.append(arr[i][j])
    return flat


def col_sum(arr):
    output = []
    for j in range(len(arr[0])):
        total = 0
        for i in range(len(arr)):
            total += arr[i][j]
        output.append(total)
    return output


num = int(sys.stdin.readline())
cur_matrix = None
for _ in range(num):
    r, c = sys.stdin.readline().split(" ")
    r, c = int(r), int(c)
    new_matrix = []
    for _ in range(r):
        row = sys.stdin.readline().split(" ")
        row = [int(row[k]) for k in range(c)]
        new_matrix.append(row)
    if cur_matrix:
        cur_matrix = tensor_product(cur_matrix, new_matrix)
    else:
        cur_matrix = deep_copy(new_matrix)

max_elem = max(flatten(cur_matrix))
min_elem = min(flatten(cur_matrix))
max_row_sum = max([sum(row) for row in cur_matrix])
min_row_sum = min([sum(row) for row in cur_matrix])
max_col_sum = max(col_sum(cur_matrix))
min_col_sum = min(col_sum(cur_matrix))

print(max_elem, min_elem, max_row_sum, min_row_sum, max_col_sum, min_col_sum, sep="\n")
