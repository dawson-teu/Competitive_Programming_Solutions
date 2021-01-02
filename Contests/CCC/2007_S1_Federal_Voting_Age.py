n = int(input())
for i in range(n):
    line = input()
    y, m, d = [int(line.split(" ")[i]) for i in range(3)]
    if y < 1989:
        print("Yes")
    elif y > 1989:
        print("No")
    elif m < 2:
        print("Yes")
    elif m > 2:
        print("No")
    elif d <= 27:
        print("Yes")
    else:
        print("No")
