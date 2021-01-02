snakes_and_ladders = {
    9: 34,
    40: 64,
    67: 86,
    54: 19,
    90: 48,
    99: 77,
}

pos = 1
while not pos == 100:
    move = int(input())
    if move == 0:
        print("You Quit!")
        break
    if pos + move <= 100:
        pos += move
    if pos in snakes_and_ladders:
        pos = snakes_and_ladders[pos]
    print("You are now on square " + str(pos))
    if pos == 100:
        print("You Win!")
