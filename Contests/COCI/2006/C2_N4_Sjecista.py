n = int(input())
total = 0
for i in range(1, n):
    total += ((i - 1) * (n - i - 1))
print(total * n // 4)
