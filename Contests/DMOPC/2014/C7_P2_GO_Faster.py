n = int(input())
passengers = []
for i in range(n - 1):
    line = input().split(" ")
    passengers.append([int(line[i]) for i in range(2)])

max_on, max_off = passengers[0]
min_on, min_off = passengers[0]
for i in range(1, n - 1):
    value = min(passengers[i][1], max_on)
    max_on -= value
    max_off -= passengers[i][1] - value
    max_off += passengers[i][0]

    value = min(passengers[i][1], min_off)
    min_off -= value
    min_on -= passengers[i][1] - value
    min_off += passengers[i][0]

print(max_on)
print(min_on)
