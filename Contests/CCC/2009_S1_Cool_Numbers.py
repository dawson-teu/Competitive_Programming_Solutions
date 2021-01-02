a = int(input())
b = int(input())

power_6 = set()
for i in range(1, 23):
    power_6.add(i ** 6)

count = 0
for i in range(a, b + 1):
    if i in power_6:
        count += 1
print(count)
