n = int(input())
total = 0
for i in range(n):
    total += float(input()) % 360
    total %= 360
print("{0:.5f}".format(round(total, 5)))
