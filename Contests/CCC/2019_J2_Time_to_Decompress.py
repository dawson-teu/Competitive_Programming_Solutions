a = int(input())

output = []
for i in range(a):
    data = input().split(" ")
    n = int(data[0])
    output.append("".join([data[1] for j in range(n)]))

for elem in output:
    print(elem)
