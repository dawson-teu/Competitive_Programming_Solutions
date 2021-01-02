def fill_board(queen_x, queen_y):
    board[queen_y][queen_x] = 1
    for i in range(n):
        board[queen_y][i] = 1
        board[i][queen_x] = 1

    for i in range(-n, n + 1):
        if 0 <= queen_y + i < n and 0 <= queen_x + i < n:
            board[queen_y + i][queen_x + i] = 1
        if 0 <= queen_y + i < n and 0 <= queen_x - i < n:
            board[queen_y + i][queen_x - i] = 1


line = input()
n, m = [int(line.split(" ")[i]) for i in range(2)]

board = []
for i in range(n):
    board.append([0 for j in range(n)])

for i in range(m):
    line = input()
    x, y = [int(line.split(" ")[i]) for i in range(2)]
    fill_board(x - 1, y - 1)

total = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            total += 1
print(total)
