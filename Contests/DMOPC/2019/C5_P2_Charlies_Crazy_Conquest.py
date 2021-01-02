line = input()
[n, h] = [int(line.split(" ")[i]) for i in range(2)]

moves = []
for i in range(n * 2):
    moves.append(0)

for i in range(n):
    moves[i * 2] = input().split(" ")

for i in range(n):
    moves[i * 2 + 1] = input().split(" ")

c_h = h
o_h = h
for i in range(n * 2):
    if moves[i][0] == "A":
        if i % 2 == 0:
            o_h -= int(moves[i][1])
        else:
            c_h -= int(moves[i][1])
    else:
        if i + 1 < (n * 2) and moves[i + 1][0] == "A":
            moves[i + 1][1] = "0"
        elif i % 2 == 0:
            c_h -= int(moves[i][1])
        else:
            o_h -= int(moves[i][1])
    if c_h <= 0:
        print("DEFEAT")
        break
    elif o_h <= 0:
        print("VICTORY")
        break
if c_h > 0 and o_h > 0:
    print("TIE")
