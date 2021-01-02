import sys

n = int(sys.stdin.readline())
arr = [0]
for i in range(n):
    arr.append(arr[i] + int(input()))

q = int(sys.stdin.readline())
output = []
for i in range(q):
    line = sys.stdin.readline()
    a, b = [int(line.split(" ")[i]) for i in range(2)]
    output.append(arr[b + 1] - arr[a])

for elem in output:
    print(elem)
