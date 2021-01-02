for _ in range(5):
    line = input().split(" ")
    r, c, num = [int(line[i]) for i in range(3)]
    row = set()
    col = set()
    for i in range(num):
        line = input().split(" ")
        x, y = [int(line[i]) for i in range(2)]
        row.add(x)
        col.add(y)
    print((r - len(row)) * (c - len(col)))
