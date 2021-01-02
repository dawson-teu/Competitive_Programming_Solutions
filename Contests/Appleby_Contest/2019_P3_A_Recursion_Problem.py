line = input().replace("(", "").replace(")", "").replace("+", "").split(" ")

total = 0
for char in line:
    if not char == "":
        total += int(char)
print(total)
