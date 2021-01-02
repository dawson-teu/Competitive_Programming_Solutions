n, m = [int(num) for num in input().split(" ")[0:2]]

start = (0, 0)
matrix = []
empty_cells = []
cameras = []
for i in range(n):
    line = input()
    line_arr = []
    for j in range(m):
        if line[j] == 'S':
            start = (i, j)
        if line[j] == '.':
            empty_cells.append((i, j))
        line_arr.append(line[j])
    matrix.append(line_arr)

print(empty_cells)
