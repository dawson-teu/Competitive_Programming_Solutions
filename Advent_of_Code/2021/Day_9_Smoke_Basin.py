with open("InputFiles/Day_9.txt") as f:
    heightmap = []
    for line in f:
        heightmap.append([int(num) for num in line.rstrip()])
    height = len(heightmap)
    width = len(heightmap[0])

part_1_ans = 0
for i in range(height):
    for j in range(width):
        is_low_point = True
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + move[0], j + move[1]
            if 0 <= new_i < height and 0 <= new_j < width and heightmap[new_i][new_j] <= heightmap[i][j]:
                is_low_point = False
                break
        if is_low_point:
            part_1_ans += 1 + heightmap[i][j]
print(part_1_ans)

visited = [[False for _ in range(width)] for _ in range(height)]
basins = []
for i in range(height):
    for j in range(width):
        is_low_point = True
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + move[0], j + move[1]
            if 0 <= new_i < height and 0 <= new_j < width and heightmap[new_i][new_j] <= heightmap[i][j]:
                is_low_point = False
                break
        if is_low_point:
            queue = [(i, j)]
            size = 0
            while len(queue) > 0:
                cur_pos = queue.pop(0)
                size += 1
                for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_pos = (cur_pos[0] + move[0], cur_pos[1] + move[1])
                    valid = 0 <= new_pos[0] < height and 0 <= new_pos[1] < width and not visited[new_pos[0]][new_pos[1]]
                    if valid and 9 > heightmap[new_pos[0]][new_pos[1]] > heightmap[cur_pos[0]][cur_pos[1]]:
                        visited[new_pos[0]][new_pos[1]] = True
                        queue.append(new_pos)
            basins.append(size)
basins = sorted(basins, reverse=True)
part_2_ans = basins[0] * basins[1] * basins[2]
print(part_2_ans)
