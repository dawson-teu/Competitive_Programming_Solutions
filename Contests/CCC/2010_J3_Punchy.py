a = 0
b = 0
line = input().split(" ")
while not line[0] == "7":
    if line[0] == "1":
        if line[1] == "A":
            a = int(line[2])
        elif line[1] == "B":
            b = int(line[2])
    elif line[0] == "2":
        if line[1] == "A":
            print(a)
        elif line[1] == "B":
            print(b)
    elif line[0] == "3":
        if line[1] == "A" and line[2] == "A":
            a = a + a
        elif line[1] == "A" and line[2] == "B":
            a = a + b
        elif line[1] == "B" and line[2] == "A":
            b = b + a
        elif line[1] == "B" and line[2] == "B":
            b = b + b
    elif line[0] == "4":
        if line[1] == "A" and line[2] == "A":
            a = a * a
        elif line[1] == "A" and line[2] == "B":
            a = a * b
        elif line[1] == "B" and line[2] == "A":
            b = b * a
        elif line[1] == "B" and line[2] == "B":
            b = b * b
    elif line[0] == "5":
        if line[1] == "A" and line[2] == "A":
            a = a - a
        elif line[1] == "A" and line[2] == "B":
            a = a - b
        elif line[1] == "B" and line[2] == "A":
            b = b - a
        elif line[1] == "B" and line[2] == "B":
            b = b - b
    elif line[0] == "6":
        if line[1] == "A" and line[2] == "A":
            a = a // a
        elif line[1] == "A" and line[2] == "B":
            a = a // b
        elif line[1] == "B" and line[2] == "A":
            b = b // a
        elif line[1] == "B" and line[2] == "B":
            b = b // b
    line = input().split(" ")
