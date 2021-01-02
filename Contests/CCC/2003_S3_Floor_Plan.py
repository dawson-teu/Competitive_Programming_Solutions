def flood_fill(tiles, start):
    area = []
    tiles_queue = [start]
    area.append(start)
    while len(tiles_queue) > 0:
        tile = tiles_queue.pop()
        if tile[1] - 1 >= 0 and not (tile[0], tile[1] - 1) in area and tiles[tile[1] - 1][tile[0]] == '.':
            tiles_queue.append((tile[0], tile[1] - 1))
            # noinspection PyUnresolvedReferences
            area.append((tile[0], tile[1] - 1))
        if tile[1] + 1 < len(tiles) and not (tile[0], tile[1] + 1) in area and tiles[tile[1] + 1][tile[0]] == '.':
            tiles_queue.append((tile[0], tile[1] + 1))
            area.append((tile[0], tile[1] + 1))
        if tile[0] + 1 < len(tiles[0]) and not (tile[0] + 1, tile[1]) in area and tiles[tile[1]][tile[0] + 1] == '.':
            tiles_queue.append((tile[0] + 1, tile[1]))
            area.append((tile[0] + 1, tile[1]))
        if tile[0] - 1 >= 0 and not (tile[0] - 1, tile[1]) in area and tiles[tile[1]][tile[0] - 1] == '.':
            tiles_queue.append((tile[0] - 1, tile[1]))
            area.append((tile[0] - 1, tile[1]))
    return area


amount_flooring = int(input())
size_y = int(input())
size_x = int(input())
floor = []
for i in range(size_y):
    floor.append(input())

rooms = []
for y in range(size_y):
    for x in range(size_x):
        if floor[y][x] == '.' and not (x, y) in [pos for room in rooms for pos in room]:
            rooms.append(flood_fill(floor, (x, y)))

rooms = [len(room) for room in rooms]
rooms.sort(reverse=True)
if sum(rooms) <= amount_flooring:
    print(str(len(rooms)) + (" rooms, " if not len(rooms) == 1 else " room, ") + str(
        amount_flooring - sum(rooms)) + " square metre(s) left over")
else:
    flooring_used = 0
    for i in range(len(rooms)):
        if flooring_used + rooms[i] >= amount_flooring:
            print(str(i) + (" rooms, " if not i == 1 else " room, ") + str(
                amount_flooring - flooring_used) + " square metre(s) left over")
            break
        flooring_used += rooms[i]
