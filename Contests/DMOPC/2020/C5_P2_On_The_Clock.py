n, m = map(int, input().split())

count = 0
output = []
for i in range(m):
    for j in range(n * i // m, (n * (i + 1) // m if n * (i + 1) % m == 0 else n * (i + 1) // m + 1)):
        count += 1
        output.append(str(j + 1) + " " + str(i + 1))
print(count)
for elem in output:
    print(elem)
