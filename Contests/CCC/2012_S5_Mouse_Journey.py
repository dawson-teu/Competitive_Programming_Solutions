import sys

r, c = sys.stdin.readline().split(" ")
r, c = int(r), int(c)
k = int(sys.stdin.readline())
cats = [sys.stdin.readline().split(" ") for _ in range(k)]
cats = set((int(b) - 1, int(a) - 1) for a, b in cats)

grid = [[0 for _ in range(c)] for _ in range(r)]
grid[0][0] = 1
for i in range(1, c):
    if (i, 0) not in cats:
        grid[0][i] = grid[0][i - 1]
for i in range(1, r):
    if (0, i) not in cats:
        grid[i][0] = grid[i - 1][0]
for i in range(1, c):
    for j in range(1, r):
        if (i, j) not in cats:
            grid[j][i] = grid[j - 1][i] + grid[j][i - 1]
print(grid[r - 1][c - 1])
