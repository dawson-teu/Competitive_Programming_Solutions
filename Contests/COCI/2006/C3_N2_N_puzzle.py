puzzle = "".join([input() for i in range(4)])
correct_puzzle = "".join(["ABCD", "EFGH", "IJKL", "MNO."])
total = 0
for i in range(len(puzzle)):
    if not puzzle[i] == ".":
        i2 = correct_puzzle.index(puzzle[i])
        total += abs(i % 4 - i2 % 4) + abs(i // 4 - i2 // 4)
print(total)
