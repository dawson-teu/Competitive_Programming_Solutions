k = int(input())

output = []
for i in range(k):
    size = input().split(" ")
    n = int(size[0])
    m = int(size[1])
    output.append(min((n - 1) * 2, (m - 1) * 2))

for elem in output:
    print(elem)
