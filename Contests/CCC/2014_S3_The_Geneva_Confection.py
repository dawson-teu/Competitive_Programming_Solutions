import sys

data_pointer = 0
all_data = sys.stdin.read().split("\n")
t = int(all_data[data_pointer])
data_pointer += 1

for i in range(t):
    n = int(all_data[data_pointer])
    data_pointer += 1

    cars = []
    for j in range(n):
        cars.append(int(all_data[data_pointer]))
        data_pointer += 1

    mountainPos = n - 1
    branch = []
    car = 1
    while car <= n:
        if mountainPos >= 0 and cars[mountainPos] == car:
            mountainPos -= 1
            car += 1
        elif len(branch) > 0 and branch[-1] == car:
            branch.pop()
            car += 1
        elif mountainPos >= 0:
            branch.append(cars[mountainPos])
            mountainPos -= 1
        else:
            break
    if car > n:
        print('Y')
    else:
        print('N')
