import sys

line = sys.stdin.readline()
n, q = [int(line.split(" ")[i]) for i in range(2)]
ratings = input().split(" ")

max_left = [0 for i in range(n)]
freq_left = [0 for i in range(n)]
max_left[0] = int(ratings[0])
freq_left[0] = 1
for i in range(1, n):
    if int(ratings[i]) > max_left[i - 1]:
        max_left[i] = int(ratings[i])
        freq_left[i] = 1
    elif int(ratings[i]) == max_left[i - 1]:
        max_left[i] = max_left[i - 1]
        freq_left[i] = freq_left[i - 1] + 1
    else:
        max_left[i] = max_left[i - 1]
        freq_left[i] = freq_left[i - 1]

max_right = [0 for i in range(n)]
freq_right = [0 for i in range(n)]
max_right[-1] = int(ratings[-1])
freq_right[-1] = 1
for i in range(n - 2, -1, -1):
    if int(ratings[i]) > max_right[i + 1]:
        max_right[i] = int(ratings[i])
        freq_right[i] = 1
    elif int(ratings[i]) == max_right[i + 1]:
        max_right[i] = max_right[i + 1]
        freq_right[i] = freq_right[i + 1] + 1
    else:
        max_right[i] = max_right[i + 1]
        freq_right[i] = freq_right[i + 1]

max_left = [0] + max_left + [0]
max_right = [0] + max_right + [0]
freq_left = [0] + freq_left + [0]
freq_right = [0] + freq_right + [0]

output = []
for i in range(q):
    line = sys.stdin.readline()
    a, b = [int(line.split(" ")[i]) for i in range(2)]
    max_rating = max(max_left[a - 1], max_right[b + 1])

    max_freq = 0
    if max_left[a - 1] > max_right[b + 1]:
        max_freq = freq_left[a - 1]
    elif max_left[a - 1] < max_right[b + 1]:
        max_freq = freq_right[b + 1]
    elif max_left[a - 1] == max_right[b + 1]:
        max_freq = freq_left[a - 1] + freq_right[b + 1]
    output.append(str(max_rating) + " " + str(max_freq))

for elem in output:
    print(elem)
