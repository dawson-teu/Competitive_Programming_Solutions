n = int(input())
x, y = map(int, input().split())

t = int(input())
total = 0
for i in range(t):
    l, r = map(int, input().split())
    total += max(min(y, r) - max(x, l) + 1, 0)
print(total)
