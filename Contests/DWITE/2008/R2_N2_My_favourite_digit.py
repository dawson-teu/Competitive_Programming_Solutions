output = []
for i in range(5):
    num = int(input())
    output.append(sorted([int(val) for val in str(num)])[-1])

for elem in output:
    print(elem)
