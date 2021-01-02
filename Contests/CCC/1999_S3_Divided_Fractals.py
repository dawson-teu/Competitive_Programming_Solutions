fractal = []


def remove_fractal(pos, level):
    if level < 1:
        return
    for j in range(pos[0] + (3 ** level) // 3, pos[0] + 2 * (3 ** level) // 3):
        for k in range(pos[1] + (3 ** level) // 3, pos[1] + 2 * (3 ** level) // 3):
            fractal[j][k] = " "

    for j in range(3):
        for k in range(3):
            remove_fractal([pos[0] + j * (3 ** level) // 3, pos[1] + j * (3 ** level) // 3], level - 1)


d = int(input())
for _ in range(d):
    n = int(input())
    fractal = []
    for _ in range(3 ** n):
        fractal.append(["*" for j in range(3 ** n)])
    remove_fractal([0, 0], n)

    b = int(input())
    t = int(input())
    left = int(input())
    r = int(input())
    output = []
    for i in range(t - 1, b - 2, -1):
        line = []
        for j in range(left - 1, r):
            line.append(fractal[i][j])
        output.append(" ".join(line))

    for elem in output:
        print(elem)
    print("\n")
