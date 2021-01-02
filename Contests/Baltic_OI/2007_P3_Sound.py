import sys

line = sys.stdin.readline()
n, m, c = [int(line.split(" ")[i]) for i in range(3)]
line = sys.stdin.readline()
samples = [int(line.split(" ")[i]) for i in range(n)]

min_q = []
max_q = []
q = []
output = []
for i in range(n):
    q.append(samples[i])
    while len(min_q) > 0 and min_q[-1] > samples[i]:
        min_q.pop()
    while len(max_q) > 0 and max_q[-1] < samples[i]:
        max_q.pop()
    min_q.append(samples[i])
    max_q.append(samples[i])

    if i >= m:
        if q[0] == min_q[0]:
            min_q.pop(0)
        if q[0] == max_q[0]:
            max_q.pop(0)
        q.pop(0)

    if i >= m - 1 and (max_q[0] - min_q[0] <= c):
        output.append(i + 2 - m)

if len(output) == 0:
    print("NONE")
else:
    for elem in output:
        print(elem)
