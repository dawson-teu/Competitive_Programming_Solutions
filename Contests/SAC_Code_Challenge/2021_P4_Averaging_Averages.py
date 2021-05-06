import sys

n, q = map(int, sys.stdin.readline().split())
averages = []
for avg in sys.stdin.readline().split():
    averages.append(int(avg))
psa = [0]
for i in range(len(averages)):
    psa.append(psa[i] + averages[i])
for i in range(q):
    l, r = sys.stdin.readline().split()
    print((psa[int(r)] - psa[int(l) - 1]) // (int(r) - int(l) + 1))
