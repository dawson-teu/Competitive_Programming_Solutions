import sys

n = int(sys.stdin.readline())
line = sys.stdin.readline()
a = line.split(" ")
line = sys.stdin.readline()
b = line.split(" ")

k = 0
total_a = 0
total_b = 0
for i in range(len(a)):
    total_a += int(a[i])
    total_b += int(b[i])
    if total_a == total_b:
        k = i + 1
print(k)
