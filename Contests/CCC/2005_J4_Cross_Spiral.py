width = int(input())
height = int(input())
rect_width = int(input())
rect_height = int(input())
steps = int(input())

grid = [[False for i in range(width)] for j in range(height)]
for i in range(height):
    for j in range(width):
        if (i < rect_height or height - rect_height - 1 < i) and (j < rect_width or width - rect_width - 1 < j):
            grid[i][j] = False
        else:
            grid[i][j] = True

pos = (rect_width, 0)
preferences = {"U": "LUR", "R": "URD", "D": "RDL", "L": "DLU"}
dir_to_num = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
cur_direction = "R"
for _ in range(steps):
    is_moved = False
    for direction in preferences[cur_direction]:
        new_pos = (pos[0] + dir_to_num[direction][0], pos[1] + dir_to_num[direction][1])
        if 0 <= new_pos[0] < width and 0 <= new_pos[1] < height and grid[new_pos[1]][new_pos[0]]:
            cur_direction = direction
            grid[pos[1]][pos[0]] = False
            pos = new_pos
            is_moved = True
            break
    if not is_moved:
        break
print(pos[0] + 1)
print(pos[1] + 1)
