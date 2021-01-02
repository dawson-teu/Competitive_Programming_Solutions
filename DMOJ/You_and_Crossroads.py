def quadrant(x, y):
    if x < n and y < n:
        return 2
    elif x < n <= y:
        return 3
    elif x >= n > y:
        return 1
    else:
        return 4


n = int(input())

matrix = []
for i in range(n * 2):
    matrix.append([char for char in input()])

quadrants = {}
for i in range(n * 2):
    for j in range(n * 2):
        if matrix[i][j] == "g" and quadrant(j, i) not in quadrants:
            quadrants[quadrant(j, i)] = 1
        elif matrix[i][j] == "g":
            quadrants[quadrant(j, i)] += 1

maximum = [0, -1]
for (key, val) in quadrants.items():
    if val > maximum[1]:
        maximum = [key, val]
print(maximum[0])
