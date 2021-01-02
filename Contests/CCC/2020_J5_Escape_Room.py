from functools import reduce


def neighbours(pos):
    value = grid[pos[1]][pos[0]]
    neighbours_list = []
    for factor in list(factors[value - 1]):
        if 0 <= factor - 1 < n and 0 <= (value // factor) - 1 < m:
            neighbours_list.append([factor - 1, value // factor - 1])
    return neighbours_list


def index(pos):
    return pos[1] * m + pos[0]


m = int(input())
n = int(input())
grid = []
max_int = -1
for i in range(m):
    line = input()
    arr = []
    for j in range(n):
        arr.append(int(line.split(" ")[j]))
        max_int = max(max_int, int(line.split(" ")[j]))
    grid.append(arr)

factors = [set(reduce(list.__add__, ([x, value // x] for x in range(1, int(value ** 0.5) + 1) if value % x == 0))) for
           value in range(1, max_int + 1)]

visited = [False for i in range(m * n)]
queue = [[0, 0]]
escape = False
while len(queue) > 0:
    v = queue.pop(0)
    if v == [n - 1, m - 1]:
        escape = True
    for neighbour in neighbours(v):
        if not visited[index(neighbour)]:
            visited[index(neighbour)] = True
            queue.append(neighbour)
print("yes" if escape else "no")
