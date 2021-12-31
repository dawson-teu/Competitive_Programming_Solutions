def fold_grid(instruction, in_dots, old_width, old_height):
    orientation, line_pos = instruction
    out_dots = set()
    for dot in in_dots:
        x, y = dot
        # Depending on line orientation we either fold the paper left or up
        # The coordinate transform is based on two simple ideas:
        # If a dot is left of or above the line, it is on the part of the paper that doesn't move
        # -> Its coordinates are unchanged
        # If a dot is right of or below the line, it is on the part of the paper that does move
        # -> Like in a reflection, the distance the dot was previously right of or below the line
        # -> is now the distance the dot is left of or above the line
        if orientation == 'x':
            if x < line_pos:
                out_dots.add((x, y))
            elif x > line_pos:
                out_dots.add((line_pos - (x - line_pos), y))
        elif orientation == 'y':
            if y < line_pos:
                out_dots.add((x, y))
            elif y > line_pos:
                out_dots.add((x, line_pos - (y - line_pos)))

    new_width = old_width
    new_height = old_height
    if orientation == 'x':
        new_width = max(line_pos, old_width - line_pos - 1)
    elif orientation == 'y':
        new_height = max(line_pos, old_height - line_pos - 1)
    return out_dots, new_width, new_height


with open("InputFiles/Day_13.txt") as f:
    dots = set()
    width = -1
    height = -1
    while (line := f.readline().rstrip()) != '':
        dot_x, dot_y = [int(num) for num in line.split(',')]
        dots.add((dot_x, dot_y))

        width = max(width, dot_x)
        height = max(height, dot_y)

    folds = []
    for line in f:
        direction, location = line.rstrip().split(' ')[2].split('=')
        folds.append((direction, int(location)))

# Part 1
dots, width, height = fold_grid(folds[0], dots, width, height)
part_1_ans = len(dots)
print(part_1_ans)

# Part 2
for fold in folds[1:]:
    dots, width, height = fold_grid(fold, dots, width, height)

# For Part 2, the answer is the 8 capital letters represented as ASCII in the grid of dots
# The grid of dots is printed to the console, and the answer must be manually read out
for i in range(height):
    line = ''
    for j in range(width):
        line += '██' if (j, i) in dots else '  '
    print(line)
