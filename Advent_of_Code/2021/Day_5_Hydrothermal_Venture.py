def cmp(x, y):
    return 1 if x > y else -1


with open("InputFiles/Day_5.txt") as f:
    lines = []
    max_width = -1
    max_height = -1
    for line in f:
        end1, end2 = line.split(" -> ")
        end1_x, end1_y = map(int, end1.split(','))
        end2_x, end2_y = map(int, end2.split(','))
        lines.append((end1_x, end1_y, end2_x, end2_y))

        max_width = max(max_width, end1_x, end2_x)
        max_height = max(max_height, end1_y, end2_y)
    max_width += 1
    max_height += 1

# part 1
num_covered = [[0 for _ in range(max_width)] for _ in range(max_height)]
for line in lines:
    end1_x, end1_y, end2_x, end2_y = line
    if end1_x == end2_x:
        for i in range(min(end1_y, end2_y), max(end1_y, end2_y) + 1):
            num_covered[i][end1_x] += 1
    elif end1_y == end2_y:
        for i in range(min(end1_x, end2_x), max(end1_x, end2_x) + 1):
            num_covered[end1_y][i] += 1

part_1_ans = 0
for i in range(max_height):
    for j in range(max_width):
        if num_covered[i][j] >= 2:
            part_1_ans += 1
print(part_1_ans)

# part 2
num_covered = [[0 for _ in range(max_width)] for _ in range(max_height)]
for line in lines:
    end1_x, end1_y, end2_x, end2_y = line
    if end1_x == end2_x:
        for i in range(min(end1_y, end2_y), max(end1_y, end2_y) + 1):
            num_covered[i][end1_x] += 1
    elif end1_y == end2_y:
        for i in range(min(end1_x, end2_x), max(end1_x, end2_x) + 1):
            num_covered[end1_y][i] += 1
    else:
        # for a diagonal line, we iterate from the 'start' (i=0) to the 'end' (i=line length)
        # for every iteration, the current position is obtained by either incrementing or decrementing from the start
        # separately for both coordinates depending on the line direction
        for i in range(abs(end2_x - end1_x) + 1):
            num_covered[end1_y + cmp(end2_y, end1_y) * i][end1_x + cmp(end2_x, end1_x) * i] += 1

part_2_ans = 0
for i in range(max_height):
    for j in range(max_width):
        if num_covered[i][j] >= 2:
            part_2_ans += 1
print(part_2_ans)
