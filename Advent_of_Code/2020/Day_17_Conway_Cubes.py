def num_neighbours_3d(position, active):
    count = 0
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                new_position = (position[0] + a, position[1] + b, position[2] + c)
                if new_position in active and not (a, b, c) == (0, 0, 0):
                    count += 1
    return count


def num_neighbours_4d(position, active):
    count = 0
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                for d in [-1, 0, 1]:
                    new_position = (position[0] + a, position[1] + b, position[2] + c, position[3] + d)
                    if new_position in active and not (a, b, c, d) == (0, 0, 0, 0):
                        count += 1
    return count


active_cells_part_1 = set()
active_cells_part_2 = set()
line = input()
i = 0
size_part_1 = len(line)
size_part_2 = len(line)
while not line == "":
    for j in range(len(line)):
        if line[j] == "#":
            active_cells_part_1.add((j - size_part_1 // 2, i - size_part_1 // 2, 0))
            active_cells_part_2.add((j - size_part_1 // 2, i - size_part_1 // 2, 0, 0))
    line = input()
    i += 1

# part 1
for _ in range(6):
    new_active_cells = set()
    for i in range(-size_part_1 + 1, size_part_1):
        for j in range(-size_part_1 + 1, size_part_1):
            for k in range(-size_part_1 + 2, size_part_1 - 1):
                result = num_neighbours_3d((i, j, k), active_cells_part_1)
                if (i, j, k) in active_cells_part_1 and (result == 2 or result == 3):
                    new_active_cells.add((i, j, k))
                if (i, j, k) not in active_cells_part_1 and result == 3:
                    new_active_cells.add((i, j, k))
    active_cells_part_1 = new_active_cells
    size_part_1 += 1
part_1_ans = len(active_cells_part_1)
print(part_1_ans)

# part 2
for y in range(6):
    new_active_cells = set()
    for i in range(-size_part_2 + 1, size_part_2):
        for j in range(-size_part_2 + 1, size_part_2):
            for k in range(-size_part_2 + 1, size_part_2):
                for m in range(-size_part_2 + 2, size_part_2 - 1):
                    result = num_neighbours_4d((i, j, k, m), active_cells_part_2)
                    if (i, j, k, m) in active_cells_part_2 and (result == 2 or result == 3):
                        new_active_cells.add((i, j, k, m))
                    if (i, j, k, m) not in active_cells_part_2 and result == 3:
                        new_active_cells.add((i, j, k, m))
    active_cells_part_2 = new_active_cells
    size_part_2 += 1
part_2_ans = len(active_cells_part_2)
print(part_2_ans)
