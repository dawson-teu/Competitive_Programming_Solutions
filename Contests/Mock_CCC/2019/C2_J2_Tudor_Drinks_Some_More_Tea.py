prev = "T"
total = 0
for i in range(7):
    char = input()
    if char == "J" and prev == "T":
        total += 1
    prev = char
print(total)
