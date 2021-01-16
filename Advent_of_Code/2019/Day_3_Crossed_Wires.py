def points_in_line(in_pos, in_dir, in_val, total_num_steps):
    output = {}
    num_steps = total_num_steps
    if in_dir == "R":
        for i in range(in_pos[0], in_pos[0] + in_val + 1):
            output[(i, in_pos[1])] = num_steps
            num_steps += 1
    elif in_dir == "L":
        for i in range(in_pos[0], in_pos[0] - in_val - 1, -1):
            output[(i, in_pos[1])] = num_steps
            num_steps += 1
    elif in_dir == "U":
        for i in range(in_pos[1], in_pos[1] + in_val + 1):
            output[(in_pos[0], i)] = num_steps
            num_steps += 1
    elif in_dir == "D":
        for i in range(in_pos[1], in_pos[1] - in_val - 1, -1):
            output[(in_pos[0], i)] = num_steps
            num_steps += 1
    return output


def update_pos(current_pos, in_dir, in_val):
    if in_dir == "L":
        return current_pos[0] - in_val, current_pos[1]
    elif in_dir == "R":
        return current_pos[0] + in_val, current_pos[1]
    elif in_dir == "U":
        return current_pos[0], current_pos[1] + in_val
    elif in_dir == "D":
        return current_pos[0], current_pos[1] - in_val


def man_dist(p):
    return abs(p[0]) + abs(p[1])


with open("InputFiles/Day_3.txt") as f:
    input_file = list(f)
    wire1 = input_file[0].strip("\n").split(",")
    wire2 = input_file[1].strip("\n").split(",")

cur_pos = (0, 0)
visited_points = set()
point_steps_dict_1 = {}
steps_count = 0
for movement in wire1:
    direction = movement[0]
    value = int(movement[1:])
    point_steps = points_in_line(cur_pos, direction, value, steps_count)
    visited_points.update(point_steps.keys())
    point_steps_dict_1 = point_steps | point_steps_dict_1
    cur_pos = update_pos(cur_pos, direction, value)
    steps_count += value

visited_points.remove((0, 0))  # prevents the central port from being counted as an intersection point
cur_pos = (0, 0)
intersection_points = []
point_steps_dict_2 = {}
steps_count = 0
for movement in wire2:
    direction = movement[0]
    value = int(movement[1:])
    point_steps = points_in_line(cur_pos, direction, value, steps_count)
    point_steps_dict_2 = point_steps | point_steps_dict_2
    for point in list(point_steps.keys()):
        if point in visited_points:
            intersection_points.append(point)
    cur_pos = update_pos(cur_pos, direction, value)
    steps_count += value

part_1_ans = 10e10
for intersection_point in intersection_points:
    if man_dist(intersection_point) < part_1_ans:
        part_1_ans = man_dist(intersection_point)
print(part_1_ans)

part_2_ans = 10e10
for intersection_point in intersection_points:
    if point_steps_dict_1[intersection_point] + point_steps_dict_2[intersection_point] < part_2_ans:
        part_2_ans = point_steps_dict_1[intersection_point] + point_steps_dict_2[intersection_point]
print(part_2_ans)
