import sys

n = int(input())

freq = []
for i in range(1000):
    freq.append([i + 1, 0])

for i in range(n):
    num = int(sys.stdin.readline())
    freq[num - 1][1] += 1

for i in range(1000):
    x = freq[i]
    j = i - 1
    while j >= 0 and freq[j][1] < x[1] or (freq[j][1] == x[1] and freq[j][0] < x[0]):
        freq[j + 1] = freq[j]
        j -= 1
    freq[j + 1] = x

if freq[0][1] == freq[2][1]:
    highest_i = 1
    for i in range(1, 1000):
        if freq[0][1] == freq[i][1]:
            highest_i = i
    print(abs(freq[0][0] - freq[highest_i][0]))
elif not freq[0][1] == freq[1][1] and freq[1][1] == freq[2][1]:
    highest_val = abs(freq[0][0] - freq[1][0])
    for i in range(2, 1000):
        if freq[1][1] == freq[i][1]:
            highest_val = max(highest_val, abs(freq[0][0] - freq[i][0]))
    print(highest_val)
else:
    print(abs(freq[0][0] - freq[1][0]))
