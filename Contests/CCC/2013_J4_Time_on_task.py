t = int(input())
c = int(input())
chores = sorted([int(input()) for i in range(c)])

count = 0
while t >= 0:
    t -= chores.pop(0)
    if t >= 0:
        count += 1
print(count)
