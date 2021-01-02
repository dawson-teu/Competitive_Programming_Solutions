line = input()
h = [char for char in line].count("H") % 2
v = [char for char in line].count("V") % 2

grid = [[1, 2], [3, 4]]
if h == 1:
    new_grid = [[0, 0], [0, 0]]
    new_grid[0][0] = grid[1][0]
    new_grid[0][1] = grid[1][1]
    new_grid[1][0] = grid[0][0]
    new_grid[1][1] = grid[0][1]
    grid = new_grid
if v == 1:
    new_grid = [[0, 0], [0, 0]]
    new_grid[0][0] = grid[0][1]
    new_grid[0][1] = grid[0][0]
    new_grid[1][0] = grid[1][1]
    new_grid[1][1] = grid[1][0]
    grid = new_grid

for i in range(2):
    print(" ".join([str(j) for j in grid[i]]))
