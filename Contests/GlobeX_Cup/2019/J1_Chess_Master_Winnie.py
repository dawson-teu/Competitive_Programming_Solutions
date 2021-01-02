line = input()
n, m, a, b, c = [int(line.split(" ")[i]) for i in range(5)]
line = input()
win_lose = [int(line.split(" ")[i]) for i in range(n)]
line = input()
opp = [int(line.split(" ")[i]) for i in range(c)]

for opponent in opp:
    if win_lose[opponent - 1] == 1:
        m += a
    else:
        m -= b
print(m)
