n = int(input())
villages = sorted([int(input()) for i in range(n)])

neigh = 2 * (10 ** 10)
for i in range(1, len(villages) - 1):
    neigh = min((villages[i] - villages[i - 1]) / 2 + (villages[i + 1] - villages[i]) / 2, neigh)
print("%.1f" % neigh)
