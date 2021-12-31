def check_board(in_board):
    for row in in_board:
        if all(row):
            return True

    for k in range(board_width):
        if all([in_board[m][k] for m in range(board_height)]):
            return True


with open("InputFiles/Day_4.txt") as f:
    drawn_numbers = [int(num) for num in f.readline().split(',')]

    boards = []
    cur_board = []
    for line in f:
        if line == '\n':
            if cur_board:
                boards.append(cur_board)
                cur_board = []
        else:
            cur_board.append([int(num) for num in line.split()])
    boards.append(cur_board)

num_boards = len(boards)
board_width = len(boards[0][0])
board_height = len(boards[0])

# create a mapping between numbers and board indices (position) for each board
board_num_pos = []
for board in boards:
    num_to_pos = {}
    for i in range(board_height):
        for j in range(board_width):
            num_to_pos[board[i][j]] = (i, j)
    board_num_pos.append(num_to_pos)

# part 1
board_marked_pos = [[[False for _ in range(board_width)] for _ in range(board_height)] for _ in range(num_boards)]
part_1_ans = -1
for num in drawn_numbers:
    # For every drawn number, check every board and mark it if appears and
    # if there are fully marked rows or columns, follow the steps to get the answer
    for index, board in enumerate(boards):
        if num in board_num_pos[index]:
            i, j = board_num_pos[index][num]
            board_marked_pos[index][i][j] = True
        if check_board(board_marked_pos[index]):
            total = 0
            for i in range(board_height):
                for j in range(board_width):
                    if not board_marked_pos[index][i][j]:
                        total += board[i][j]
            part_1_ans = total * num
            break
    if part_1_ans != -1:
        break
print(part_1_ans)

# part 2
board_marked_pos = [[[False for _ in range(board_width)] for _ in range(board_height)] for _ in range(num_boards)]
board_won = [False for _ in range(num_boards)]
part_2_ans = -1
for num in drawn_numbers:
    # For every drawn number, check every board and mark it if appears and
    # if there are fully marked rows or columns, mark that board as already won.
    # If after a number is drawn, the last board is won, follow the steps to get the answer
    for index, board in enumerate(boards):
        if num in board_num_pos[index]:
            i, j = board_num_pos[index][num]
            board_marked_pos[index][i][j] = True
        if check_board(board_marked_pos[index]):
            board_won[index] = True
        if all(board_won):
            total = 0
            for i in range(board_height):
                for j in range(board_width):
                    if not board_marked_pos[index][i][j]:
                        total += board[i][j]
            part_2_ans = total * num
            break
    if part_2_ans != -1:
        break
print(part_2_ans)
