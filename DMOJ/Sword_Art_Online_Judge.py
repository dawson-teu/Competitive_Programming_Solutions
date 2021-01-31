n = int(input())
total = 0
for i in range(n + 1):
    total += (i ** 6)
print(total % 1000000000)
