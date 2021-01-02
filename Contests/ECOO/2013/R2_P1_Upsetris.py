def format_board(block_values, w, h):
    board = []
    for j in range(h):
        board.append("|" + "".join(["O" if (h - j) <= block_values[num] else " " for num in range(w)]) + "|")
    board.append("|" + "".join(["=" for _ in range(w)]) + "|")
    return board


block_sums = []
heights = []
for i in range(5):
    line = input()
    block_sum = [0 for j in range(len(line) - 2)]
    height = 0
    while not (line[1] == "="):
        # noinspection PyUnresolvedReferences
        block_sum = [block_sum[j] + (1 if line[j + 1] == "O" else 0) for j in range(len(block_sum))]
        line = input()
        height += 1
    block_sums.append(list(reversed(block_sum)))
    heights.append(height)

for i in range(5):
    min_val = min(block_sums[i])
    block_sums[i] = [block_sums[i][j] - min_val for j in range(len(block_sums[i]))]

for i in range(5):
    for line in format_board(block_sums[i], len(block_sums[i]), heights[i]):
        print(line)
