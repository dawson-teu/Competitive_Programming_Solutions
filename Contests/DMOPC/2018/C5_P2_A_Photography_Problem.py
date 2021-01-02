import sys


def correction(picture, c):
    total = 0
    for i in range(n):
        for j in range(m):
            new_val = min(picture[i][j] * c, 1.0)
            total += new_val
    return total / (n * m)


dim = sys.stdin.readline().split(" ")
n = int(dim[0])
m = int(dim[1])

pic = []
for _ in range(n):
    r = sys.stdin.readline().split(" ")
    pic.append([float(r[j]) for j in range(m)])

low = 0
high = 1000
while low != high:
    middle = (low + high) / 2
    val = correction(pic, middle)
    if abs(val - 0.48) < (10 ** (-7)):
        if abs(middle - 1.0) <= (10 ** (-5)):
            print("correctly exposed")
            break
        elif middle > 1:
            print("underexposed")
        else:
            print("overexposed")
        print(middle)
        break
    elif val > 0.48:
        high = middle
    elif val < 0.48:
        low = middle
