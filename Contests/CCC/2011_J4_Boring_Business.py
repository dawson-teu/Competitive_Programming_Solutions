def index2d(x, y):
    return 401 * y + x


def check_intersection(cur_pos, direction, length):
    if direction == "r":
        for k in range(cur_pos[0], cur_pos[0] - length, -1):
            if index2d(k, cur_pos[1]) in ground:
                return False
            ground.add(index2d(k, cur_pos[1]))
    elif direction == "l":
        for k in range(cur_pos[0], cur_pos[0] + length):
            if index2d(k, cur_pos[1]) in ground:
                return False
            ground.add(index2d(k, cur_pos[1]))
    elif direction == "d":
        for k in range(cur_pos[1], cur_pos[1] + length):
            if index2d(cur_pos[0], k) in ground:
                return False
            ground.add(index2d(cur_pos[0], k))
    elif direction == "u":
        for k in range(cur_pos[1], cur_pos[1] - length, -1):
            if index2d(cur_pos[0], k) in ground:
                return False
            ground.add(index2d(cur_pos[0], k))
    return True


ground = set()
starting = [0, -1, 0, -2, 0, -3, 1, -3, 2, -3, 3, -3, 3, -4, 3, -5, 4, -5, 5, -5, 5, -4, 5, -3, 6, -3, 7, -3, 7, -4, 7,
            -5, 7, -6, 7, -7, 6, -7, 5, -7, 4, -7, 3, -7, 2, -7, 1, -7, 0, -7, -1, -7, -1, -6, -1, -5]

for i in range(0, len(starting), 2):
    ground.add(index2d(starting[i] + 200, starting[i + 1] + 201))

pos = (199, 196)
command = input().split(" ")
while not command[0] == "q":
    if command[0] == "l":
        pos = (pos[0] - int(command[1]), pos[1])
    elif command[0] == "r":
        pos = (pos[0] + int(command[1]), pos[1])
    elif command[0] == "d":
        pos = (pos[0], pos[1] - int(command[1]))
    elif command[0] == "u":
        pos = (pos[0], pos[1] + int(command[1]))
    if check_intersection(pos, command[0], int(command[1])):
        print(str(pos[0] - 200), str(pos[1] - 201), "safe")
    else:
        print(str(pos[0] - 200), str(pos[1] - 201), "DANGER")
        break
    command = input().split(" ")
