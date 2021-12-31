def step_brute_force(in_grid):
    out_grid = [row.copy() for row in in_grid]
    cur_flashed = [[False for _ in range(10)] for _ in range(10)]
    while any(energy > 9 for row in out_grid for energy in row):
        for in_i in range(10):
            for in_j in range(10):
                if out_grid[in_i][in_j] > 9:
                    for change_i in [-1, 0, 1]:
                        for change_j in [-1, 0, 1]:
                            if change_i == change_j == 0:
                                continue
                            if 0 <= in_i + change_i < 10 and 0 <= in_j + change_j < 10:
                                out_grid[in_i + change_i][in_j + change_j] += 1
                    out_grid[in_i][in_j] = -10 ** 10  # if an octopus has already flashed, set its energy to a
                    # very negative number to ensure it doesn't flash again
                    cur_flashed[in_i][in_j] = True
    return out_grid, cur_flashed


def step_bfs(in_grid):
    out_grid = [row.copy() for row in in_grid]
    cur_flashed = [[False for _ in range(10)] for _ in range(10)]
    queue = []
    for in_i in range(10):
        for in_j in range(10):
            if out_grid[in_i][in_j] > 9:
                queue.append((in_i, in_j))
                cur_flashed[in_i][in_j] = True
    while len(queue) > 0:
        cur_pos = queue.pop(0)
        for change_i in [-1, 0, 1]:
            for change_j in [-1, 0, 1]:
                if change_i == change_j == 0:
                    continue
                new_pos = (cur_pos[0] + change_i, cur_pos[1] + change_j)
                if 0 <= new_pos[0] < 10 and 0 <= new_pos[1] < 10 and not cur_flashed[new_pos[0]][new_pos[1]]:
                    out_grid[new_pos[0]][new_pos[1]] += 1
                    if out_grid[new_pos[0]][new_pos[1]] > 9:
                        queue.append(new_pos)
                        cur_flashed[new_pos[0]][new_pos[1]] = True
    return out_grid, cur_flashed


with open("InputFiles/Day_11.txt") as f:
    original_grid = []
    for line in f:
        original_grid.append([int(num) for num in line.rstrip()])

grid = [row.copy() for row in original_grid]
total_flashes = 0
for _ in range(100):
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1

    grid, flashed = step_bfs(grid)

    for i in range(10):
        for j in range(10):
            if flashed[i][j]:
                total_flashes += 1
                grid[i][j] = 0
part_1_ans = total_flashes
print(part_1_ans)

grid = [row.copy() for row in original_grid]
step = 0
while any(energy != 0 for row in grid for energy in row):
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1

    grid, flashed = step_bfs(grid)

    for i in range(10):
        for j in range(10):
            if flashed[i][j]:
                grid[i][j] = 0
    step += 1
part_2_ans = step
print(part_2_ans)
