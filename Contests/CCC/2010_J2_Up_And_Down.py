a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
nikky = [True, 0, 0]
byron = [True, 0, 0]
for i in range(s):
    nikky[2] += 1 if nikky[0] else -1
    nikky[1] += 1
    if nikky[0] and nikky[1] >= a or not nikky[0] and nikky[1] >= b:
        nikky[0] = not nikky[0]
        nikky[1] = 0

    byron[2] += 1 if byron[0] else -1
    byron[1] += 1
    if byron[0] and byron[1] >= c or not byron[0] and byron[1] >= d:
        byron[0] = not byron[0]
        byron[1] = 0

if nikky[2] > byron[2]:
    print("Nikky")
elif byron[2] > nikky[2]:
    print("Byron")
else:
    print("Tied")
