n = int(input())

total = 0
for i in range(n // 2 + 1):
    if 0 <= n - i <= 5:
        total += 1
print(total)
