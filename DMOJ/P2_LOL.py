n = int(input())

min_max_x = [1001, -1001]
min_max_y = [1001, -1001]
for i in range(n):
    pos = input().split(" ")
    x = int(pos[0])
    y = int(pos[1])
    min_max_x[0] = min(min_max_x[0], x)
    min_max_y[0] = min(min_max_y[0], y)
    min_max_x[1] = max(min_max_x[1], x)
    min_max_y[1] = max(min_max_y[1], y)
print((min_max_x[1] - min_max_x[0]) * (min_max_y[1] - min_max_y[0]))
