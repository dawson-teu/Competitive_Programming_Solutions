def chips_in_line(line):
    total_of_chips = 0
    for index in range(3):
        if line[index] == 'R' and line[index + 1] == 'R' and line[index + 2] == 'R' and line[index + 3] == 'R':
            total_of_chips += 1
    return total_of_chips


board = []
for i in range(6):
    board.append([list(input()) for j in range(6)])
    if not i == 5:
        input()

total = 0

# rows
for depth in range(6):
    for i in range(6):
        total += chips_in_line(board[depth][i])

# columns
for depth in range(6):
    for j in range(6):
        column = []
        for i in range(6):
            column.append(board[depth][i][j])
        total += chips_in_line(column)

# depths
for i in range(6):
    for j in range(6):
        depths = []
        for depth in range(6):
            depths.append(board[depth][i][j])
        total += chips_in_line(depths)

if total == 0:
    print('lost')
else:
    print(total)
