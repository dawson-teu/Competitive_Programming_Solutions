line = input()
first = [int(line.split(" ")[i]) for i in range(2)]
line = input()
second = [int(line.split(" ")[i]) for i in range(2)]

i = 0
while True:
    if i % first[1] == 0:
        second[0] -= 1
    if i % second[1] == 0:
        first[0] -= 1
    if first[0] == 0 and second[0] == 0:
        print("-1")
        break
    elif first[0] == 0:
        print("2")
        break
    elif second[0] == 0:
        print("1")
        break
    i += 1
