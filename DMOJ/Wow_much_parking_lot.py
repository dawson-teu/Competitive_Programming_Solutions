n = int(input())
pos = [0, 0]
for i in range(n):
    direction = input()
    amt = int(input())
    if direction == "North":
        pos[1] += amt
    elif direction == "East":
        pos[0] += amt
    elif direction == "South":
        pos[1] -= amt
    elif direction == "West":
        pos[0] -= amt
print(" ".join([str(num) for num in pos]))
