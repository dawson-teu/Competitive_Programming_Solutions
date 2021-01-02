h = int(input())
for i in range(h):
    line = ""
    width = (h // 2 + 1) - abs(h // 2 - i)
    line += "*" * (width * 2 - 1)
    line += " " * ((h * 2) - (2 * (width * 2 - 1)))
    line += "*" * (width * 2 - 1)
    print(line)
