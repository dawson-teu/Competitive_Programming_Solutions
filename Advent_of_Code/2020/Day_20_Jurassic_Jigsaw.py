import math


def tile_edges(in_tile):
    top_edge_out = in_tile[0]
    bottom_edge_out = in_tile[-1]
    left_edge_out = "".join([row[0] for row in in_tile])
    right_edge_out = "".join([row[-1] for row in in_tile])
    return top_edge_out, bottom_edge_out, left_edge_out, right_edge_out


def find_edge_id(in_edge):
    if in_edge in edges_id:
        return edges_id[in_edge]
    else:
        return edges_id[in_edge[::-1]]


def find_edge_count(in_edge):
    if in_edge in edges_count:
        return edges_count[in_edge]
    else:
        return edges_count[in_edge[::-1]]


def rotate_tile(in_tile):
    out_tile = [["" for _ in range(len(in_tile[0]))] for _ in range(len(in_tile))]
    for i in range(len(in_tile)):
        for j in range(len(in_tile[0])):
            out_tile[j][len(in_tile[0]) - i - 1] = in_tile[i][j]
    return ["".join(row) for row in out_tile]


def flip_x(in_tile):
    out_tile = []
    for row in in_tile:
        out_tile.append(row[::-1])
    return out_tile


def flip_y(in_tile):
    out_tile = in_tile[::-1]
    return out_tile


def orientate_tile(in_tile, condition):
    while True:
        for x_flip in range(2):
            for y_flip in range(2):
                for rotate_angle in range(4):
                    new_tile = in_tile.copy()
                    if x_flip == 1:
                        new_tile = flip_x(new_tile)
                    if y_flip == 1:
                        new_tile = flip_y(new_tile)
                    for i in range(rotate_angle):
                        new_tile = rotate_tile(new_tile)
                    if condition(new_tile):
                        return new_tile


def corner_condition(in_tile):
    (_, bottom_edge_in, _, right_edge_in) = tile_edges(in_tile)
    return find_edge_count(bottom_edge_in) == 2 and find_edge_count(right_edge_in) == 2


def edge_condition(in_tile, check_edge):
    (_, _, left_edge_in, _) = tile_edges(in_tile)
    output = True
    for i in range(len(left_edge_in)):
        if not left_edge_in[i] == check_edge[i]:
            output = False
            break
    return output


def gen_condition(in_tile, check_edge):
    (top_edge_in, _, _, _) = tile_edges(in_tile)
    output = True
    for i in range(len(top_edge_in)):
        if not top_edge_in[i] == check_edge[i]:
            output = False
            break
    return output


def find_sea_monsters(in_image):
    sea_monster = ["                  # ",
                   "#    ##    ##    ###",
                   " #  #  #  #  #  #   "]
    count = 0
    sea_monster_parts = set()
    for i in range(len(in_image) - len(sea_monster)):
        for j in range(len(in_image[0]) - len(sea_monster[0])):
            is_sea_monster = True
            pos_sea_monster_parts = set()
            for monster_i in range(len(sea_monster)):
                for monster_j in range(len(sea_monster[0])):
                    if sea_monster[monster_i][monster_j] == "#" and not in_image[i + monster_i][j + monster_j] == "#":
                        is_sea_monster = False
                        break
                    elif sea_monster[monster_i][monster_j] == "#" and in_image[i + monster_i][j + monster_j] == "#":
                        pos_sea_monster_parts.add((j + monster_j, i + monster_i))
            if is_sea_monster:
                count += 1
                sea_monster_parts.update(pos_sea_monster_parts)

    water_roughness = 0
    for i in range(len(in_image)):
        for j in range(len(in_image[0])):
            if in_image[i][j] == "#" and (j, i) not in sea_monster_parts:
                water_roughness += 1
    return count, water_roughness


tiles = {}
line = input()
while not line == "0":
    tile_id = int(line.split(" ")[1][:-1])
    tile = []
    line = input()
    while not line == "":
        tile.append(line)
        line = input()
    tiles[tile_id] = tile
    line = input()

edges_count = {}
edges_id = {}
counter = 1
for tile in tiles.values():
    (top_edge, bottom_edge, left_edge, right_edge) = tile_edges(tile)
    if top_edge not in edges_count and top_edge[::-1] not in edges_count:
        edges_count[top_edge] = 1
        edges_id[top_edge] = counter
        counter += 1
    elif top_edge in edges_count:
        edges_count[top_edge] += 1
    else:
        edges_count[top_edge[::-1]] += 1
    if bottom_edge not in edges_count and bottom_edge[::-1] not in edges_count:
        edges_count[bottom_edge] = 1
        edges_id[bottom_edge] = counter
        counter += 1
    elif bottom_edge in edges_count:
        edges_count[bottom_edge] += 1
    else:
        edges_count[bottom_edge[::-1]] += 1
    if left_edge not in edges_count and left_edge[::-1] not in edges_count:
        edges_count[left_edge] = 1
        edges_id[left_edge] = counter
        counter += 1
    elif left_edge in edges_count:
        edges_count[left_edge] += 1
    else:
        edges_count[left_edge[::-1]] += 1
    if right_edge not in edges_count and right_edge[::-1] not in edges_count:
        edges_count[right_edge] = 1
        edges_id[right_edge] = counter
        counter += 1
    elif right_edge in edges_count:
        edges_count[right_edge] += 1
    else:
        edges_count[right_edge[::-1]] += 1

# part 1
product = 1
corner_tile = []
for (key, value) in tiles.items():
    edges = tile_edges(value)
    total = 0
    for edge in edges:
        total += find_edge_count(edge)
    if total == 6:
        corner_tile = (value, key)
        product *= key
part_1_ans = product
print(part_1_ans)

# part 2

size = int(math.sqrt(len(tiles.values())))
image = [[[] for j in range(size)] for i in range(size)]
image[0][0] = orientate_tile(corner_tile[0], corner_condition)
used_tiles = {corner_tile[1]}

for i in range(1, size):
    (_, _, _, needed_edge) = tile_edges(image[0][i - 1])
    valid_tile = []
    for (key, edge_tile) in tiles.items():
        for edge in tile_edges(edge_tile):
            if find_edge_id(edge) == find_edge_id(needed_edge) and key not in used_tiles:
                valid_tile = [edge_tile, key]
                break
    image[0][i] = orientate_tile(valid_tile[0], lambda x: edge_condition(x, needed_edge))
    used_tiles.add(valid_tile[1])

for i in range(size):
    for j in range(1, size):
        (_, needed_edge, _, _) = tile_edges(image[j - 1][i])
        valid_tile = []
        for (key, tile) in tiles.items():
            for edge in tile_edges(tile):
                if find_edge_id(edge) == find_edge_id(needed_edge) and key not in used_tiles:
                    valid_tile = [tile, key]
                    break
        image[j][i] = orientate_tile(valid_tile[0], lambda x: gen_condition(x, needed_edge))
        used_tiles.add(valid_tile[1])

border_removed_image = []
for i in range(size):
    border_removed_row = []
    for j in range(size):
        border_removed_tile = []
        for tile_i in range(len(image[i][j])):
            if tile_i == 0 or tile_i == len(image[i][j]) - 1:
                continue
            border_removed_tile.append(image[i][j][tile_i][1:-1])
        border_removed_row.append(border_removed_tile)
    border_removed_image.append(border_removed_row)

final_image = []
for i in range(size * len(border_removed_image[0][0])):
    final_row = ""
    for j in range(size):
        index_1 = i // len(border_removed_image[0][0])
        index_2 = j // len(border_removed_image[0][0])
        index_3 = i % len(border_removed_image[0][0])
        final_row += border_removed_image[index_1][j][index_3]
    final_image.append(final_row)

final_image = orientate_tile(final_image, lambda in_image: find_sea_monsters(in_image)[0] > 0)
(_, part_2_ans) = find_sea_monsters(final_image)
print(part_2_ans)
