directions = []
side = input()
place = input()
while not place == "SCHOOL":
    directions.append([side, place])
    side = input()
    place = input()
directions.append([side, place])
directions.reverse()

for i in range(len(directions) - 1):
    print("Turn " + ("RIGHT" if directions[i][0] == "L" else "LEFT") + " onto " + directions[i + 1][1] + " street.")
print("Turn " + ("RIGHT" if directions[-1][0] == "L" else "LEFT") + " into your HOME.")
