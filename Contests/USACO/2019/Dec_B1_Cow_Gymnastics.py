def consistent(a, b):
    for i in range(k):
        if cows[i].index(a + 1) <= cows[i].index(b + 1):
            return False
    return True


line = input()
k, n = [int(line.split(" ")[i]) for i in range(2)]
cows = []
for i in range(k):
    line = input()
    row = [int(line.split(" ")[j]) for j in range(n)]
    cows.append(row)

total = 0
for i in range(n):
    for j in range(n):
        if consistent(i, j):
            total += 1
print(total)
