dir_to_coord = {
    "0": (0, -1, 1),
    "1": (-1, 0, 1),
    "2": (1, 0, -1),
    "3": (0, 1, -1),
    "4": (1, -1, 0),
    "5": (-1, 1, 0)
}


def add_hex(pos1, pos2):
    output1 = pos1[0] + pos2[0]
    output2 = pos1[1] + pos2[1]
    output3 = pos1[2] + pos2[2]
    return output1, output2, output3


def num_neighbours(position, active):
    count = 0
    for move_direction in dir_to_coord.values():
        new_position = add_hex(position, move_direction)
        if new_position in active:
            count += 1
    return count


commands = []
line = input()
while not line == "":
    line = line.replace("se", "0").replace("sw", "1").replace("ne", "2")
    line = line.replace("nw", "3").replace("e", "4").replace("w", "5")
    commands.append(line)
    line = input()

# Part 1
tiles = {}
max_size = -1
for command in commands:
    cur_pos = (0, 0, 0)
    for direction in command:
        movement = dir_to_coord[direction]
        cur_pos = add_hex(cur_pos, movement)
        max_size = max(max_size, max(cur_pos))
    if cur_pos in tiles:
        tiles[cur_pos] = "white" if tiles[cur_pos] == "black" else "black"
    else:
        tiles[cur_pos] = "black"

active_tiles = set()
part_1_ans = 0
for (tile, color) in tiles.items():
    if color == "black":
        part_1_ans += 1
        active_tiles.add(tile)
print(part_1_ans)

for m in range(100):
    new_active_tiles = set()
    for i in range(-max_size + 1, max_size):
        for j in range(-max_size + 1, max_size):
            pos = (i, j, -(i + j))
            result = num_neighbours(pos, active_tiles)
            if pos in active_tiles and (result == 1 or result == 2):
                new_active_tiles.add(pos)
            if pos not in active_tiles and result == 2:
                new_active_tiles.add(pos)
    active_tiles = new_active_tiles
    max_size += 1
part_2_ans = len(active_tiles)
print(part_2_ans)
