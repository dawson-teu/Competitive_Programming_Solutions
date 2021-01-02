n = int(input())
line = input()
values = [int(line.split(" ")[i]) for i in range(n)]

values = sorted(values)
low = (n + 1) // 2 - 1
high = low + 1
new_values = []
for i in range(n):
    if i % 2 == 0:
        new_values.append(str(values[low]))
        low -= 1
    else:
        new_values.append(str(values[high]))
        high += 1
print(" ".join(new_values))
