import math
import sys

n, q = sys.stdin.readline().split(" ")
n, q = int(n), int(q)
weights = sys.stdin.readline().split(" ")
freq = {}
for weight in weights:
    if int(weight) in freq:
        freq[int(weight)] += 1
    else:
        freq[int(weight)] = 1
for i in range(q):
    a, b = sys.stdin.readline().split(" ")
    if a == "1" and int(b) in freq:
        if int(math.floor(int(b) / 2)) in freq:
            freq[int(math.floor(int(b) / 2))] += freq[int(b)]
        else:
            freq[int(math.floor(int(b) / 2))] = freq[int(b)]
        if int(math.ceil(int(b) / 2)) in freq:
            freq[int(math.ceil(int(b) / 2))] += freq[int(b)]
        else:
            freq[int(math.ceil(int(b) / 2))] = freq[int(b)]
        freq[int(b)] = 0
    elif a == "2":
        print(freq[int(b)] if int(b) in freq else 0)
