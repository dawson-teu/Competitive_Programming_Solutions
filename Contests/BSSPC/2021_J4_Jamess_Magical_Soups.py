x, n = map(int, input().split())
count = 0
for i in range(n):
    t, f = map(int, input().split())
    if t - x <= f:
        count += 1
print(count)
