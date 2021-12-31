with open("InputFiles/Day_2.txt") as f:
    commands = []
    for line in f:
        direction, distance = line.split()
        commands.append((direction, int(distance)))

horizontal_pos = 0
depth = 0
for command in commands:
    direction, distance = command
    if direction == 'forward':
        horizontal_pos += distance
    elif direction == 'up':
        depth -= distance
    elif direction == 'down':
        depth += distance
part_1_ans = horizontal_pos * depth
print(part_1_ans)

aim = 0
horizontal_pos = 0
depth = 0
for command in commands:
    direction, distance = command
    if direction == 'forward':
        horizontal_pos += distance
        depth += aim * distance
    elif direction == 'up':
        aim -= distance
    elif direction == 'down':
        aim += distance
part_2_ans = horizontal_pos * depth
print(part_2_ans)
