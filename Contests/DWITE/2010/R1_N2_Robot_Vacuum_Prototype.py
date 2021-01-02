for _ in range(5):
    hallway = input()
    commands = [input() for i in range(5)]

    robot_pos = hallway.index("*")
    for i in range(5):
        if commands[i] == "L":
            robot_pos -= 1
            robot_pos = 0 if robot_pos < 0 else robot_pos
        if commands[i] == "R":
            robot_pos += 1
            robot_pos = 4 if robot_pos > 4 else robot_pos

    new_hallway = ""
    for i in range(5):
        if i == robot_pos:
            new_hallway += "*"
        else:
            new_hallway += "."
    print(new_hallway)
