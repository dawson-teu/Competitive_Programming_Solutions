n = int(input())
x = [101, 0]
y = [101, 0]
for i in range(n):
    line = input().split(",")
    # noinspection PyUnresolvedReferences
    x = [min(x[0], int(line[0])), max(x[1], int(line[0]))]
    # noinspection PyUnresolvedReferences
    y = [min(y[0], int(line[1])), max(y[1], int(line[1]))]
print(str(x[0] - 1) + "," + str(y[0] - 1))
print(str(x[1] + 1) + "," + str(y[1] + 1))
