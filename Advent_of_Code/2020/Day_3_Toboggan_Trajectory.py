def slope_count(slope, arr):
    pos = (0, 0)
    count = 0
    while pos[1] < len(arr):
        if arr[pos[1]][pos[0]] == "#":
            count += 1
        pos = (pos[0] + slope[0], pos[1] + slope[1])
        pos = (pos[0] % len(arr[0]), pos[1])
    return count


grid = []
line = input()
while not line == "":
    grid.append(line)
    line = input()

# Part 1
total_1 = slope_count((3, 1), grid)
print(total_1)

# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total_2 = 1
for s in slopes:
    total_2 *= slope_count(s, grid)
print(total_2)
