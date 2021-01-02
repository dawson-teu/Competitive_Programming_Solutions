def is_filled(x, y, mag):
    conv_x = x // (5 ** (mag - 1))
    conv_y = y // (5 ** (mag - 1))
    if mag == 1:
        return (1 <= x <= 3 and y == 0) or (x == 2 and y == 1)
    elif (1 <= conv_x <= 3 and conv_y == 0) or (conv_x == 2 and conv_y == 1):
        return True
    elif ((conv_x == 1 or conv_x == 3) and conv_y == 1) or (conv_x == 2 and conv_y == 2):
        return is_filled(x - (conv_x * (5 ** (mag - 1))), y - (conv_y * (5 ** (mag - 1))), mag - 1)
    else:
        return False


t = int(input())
output = []
for _ in range(t):
    line = input()
    m, i, j = [int(line.split(" ")[i]) for i in range(3)]
    if is_filled(i, j, m):
        output.append("crystal")
    else:
        output.append("empty")

for elem in output:
    print(elem)
