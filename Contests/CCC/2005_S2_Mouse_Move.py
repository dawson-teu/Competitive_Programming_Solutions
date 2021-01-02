line = input()
width = int(line.split(" ")[0])
height = int(line.split(" ")[1])

pos = [0, 0]
output = []
while not line == "0 0":
    line = input()
    pos[0] += int(line.split(" ")[0])
    pos[1] += int(line.split(" ")[1])
    if pos[0] > width:
        pos[0] = width
    elif pos[0] < 0:
        pos[0] = 0
    if pos[1] > height:
        pos[1] = height
    elif pos[1] < 0:
        pos[1] = 0
    output.append(str(pos[0]) + " " + str(pos[1]))

for elem in output[:-1]:
    print(elem)
