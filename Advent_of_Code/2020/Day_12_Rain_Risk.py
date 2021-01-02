def update_pos(direction, amount, position):
    position = position.copy()
    if direction == "N":
        position[1] += amount
    elif direction == "E":
        position[0] += amount
    elif direction == "S":
        position[1] -= amount
    elif direction == "W":
        position[0] -= amount
    return position


def rotate_vector(vec, direction):
    if direction == "L":
        return [-vec[1], vec[0]]
    elif direction == "R":
        return [vec[1], -vec[0]]


dir_to_angle = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
angle_to_dir = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}

nav_ins = []
line = input()
while not line == "":
    nav_ins.append(line)
    line = input()


# part 1
pos = [0, 0]
direction_angle = 90
for ins in nav_ins:
    action = ins[0]
    value = int(ins[1:])
    if action in ['N', 'E', 'S', 'W']:
        pos = update_pos(action, value, pos)
    elif action == "F":
        pos = update_pos(angle_to_dir[direction_angle % 360], value, pos)
    elif action == "L":
        direction_angle -= value
    elif action == "R":
        direction_angle += value
part_1_ans = abs(pos[0]) + abs(pos[1])
print(part_1_ans)

# part 2
pos = [0, 0]
waypoint = [10, 1]
for ins in nav_ins:
    action = ins[0]
    value = int(ins[1:])
    if action in ['N', 'E', 'S', 'W']:
        waypoint = update_pos(action, value, waypoint)
    elif action == "F":
        pos[0] += waypoint[0] * value
        pos[1] += waypoint[1] * value
    elif action in ["L", "R"]:
        for i in range((value % 360) // 90):
            waypoint = rotate_vector(waypoint, action)
part_2_ans = abs(pos[0]) + abs(pos[1])
print(part_2_ans)
