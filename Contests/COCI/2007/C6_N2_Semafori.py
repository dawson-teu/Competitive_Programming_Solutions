line = input()
n, length = [int(line.split(" ")[i]) for i in range(2)]

traffic = []
for i in range(n):
    line = input()
    traffic.append([int(line.split(" ")[i]) for i in range(3)])

time = traffic[0][0]
for i in range(n):
    light = time % (traffic[i][1] + traffic[i][2])
    if light <= traffic[i][1]:
        time += traffic[i][1] - light
    if not i == n - 1:
        time += traffic[i + 1][0] - traffic[i][0]
time += length - traffic[-1][0]
print(time)
