def pos_in_bounds(x, y, in_grid):
    return 0 <= x < len(in_grid[0]) and 0 <= y < len(in_grid)


def num_neighbours_part_1(pos, in_grid):
    check_pos = [-1, 0, 1]
    count = 0
    for y in range(3):
        for x in range(3):
            if y == 1 and x == 1:
                continue
            new_pos = [pos[0] + check_pos[y], pos[1] + check_pos[x]]
            if pos_in_bounds(new_pos[0], new_pos[1], in_grid):
                if in_grid[new_pos[1]][new_pos[0]] == "#":
                    count += 1
    return count


def num_neighbours_part_2(pos, in_grid):
    check_pos = [-1, 0, 1]
    directions = []
    for x in range(3):
        for y in range(3):
            if y == 1 and x == 1:
                continue
            directions.append([check_pos[x], check_pos[y]])

    count = 0
    for k in range(8):
        new_pos = [pos[0] + directions[k][0], pos[1] + directions[k][1]]
        while pos_in_bounds(new_pos[0], new_pos[1], in_grid):
            if in_grid[new_pos[1]][new_pos[0]] == "#":
                count += 1
                break
            if in_grid[new_pos[1]][new_pos[0]] == "L":
                break
            new_pos[0] += directions[k][0]
            new_pos[1] += directions[k][1]
    return count


def is_grid_same(old_grid, new_grid):
    is_same = True
    for y in range(len(old_grid)):
        for x in range(len(old_grid[0])):
            if not old_grid[y][x] == new_grid[y][x]:
                is_same = False
                break
    return is_same


def deep_copy(in_grid, val=None):
    new_copy = []
    for y in range(len(in_grid)):
        row = []
        for x in range(len(in_grid[0])):
            if val:
                row.append(0)
            else:
                row.append(in_grid[y][x])
        new_copy.append(row)
    return new_copy


grid = []
line = input()
while not line == "":
    grid.append([char for char in line])
    line = input()

prev = grid
cur = deep_copy(grid, 5)
part_1_ans = 0
while True:
    count_occupied = 0
    for i in range(len(prev)):
        for j in range(len(prev[0])):
            if prev[i][j] == "L" and num_neighbours_part_1((j, i), prev) == 0:
                cur[i][j] = "#"
                count_occupied += 1
            elif prev[i][j] == "#" and num_neighbours_part_1((j, i), prev) >= 4:
                cur[i][j] = "L"
            else:
                if prev[i][j] == "#":
                    count_occupied += 1
                cur[i][j] = prev[i][j]
    if is_grid_same(prev, cur):
        part_1_ans = count_occupied
        break
    prev = deep_copy(cur)
print(part_1_ans)

prev = grid
cur = deep_copy(grid, 5)
part_2_ans = 0
while True:
    count_occupied = 0
    for i in range(len(prev)):
        for j in range(len(prev[0])):
            if prev[i][j] == "L" and num_neighbours_part_2((j, i), prev) == 0:
                cur[i][j] = "#"
                count_occupied += 1
            elif prev[i][j] == "#" and num_neighbours_part_2((j, i), prev) >= 5:
                cur[i][j] = "L"
            else:
                if prev[i][j] == "#":
                    count_occupied += 1
                cur[i][j] = prev[i][j]
    if is_grid_same(prev, cur):
        part_2_ans = count_occupied
        break
    prev = deep_copy(cur)
print(part_2_ans)
