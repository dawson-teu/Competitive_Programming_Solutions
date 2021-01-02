line = input()
[n, m] = [int(line.split(" ")[i]) for i in range(2)]

items = set()
for i in range(n):
    items.add(input())

total = 0
for i in range(m):
    t = int(input())
    complete = True
    for j in range(t):
        if not input() in items:
            complete = False
    if complete:
        total += 1
print(total)
