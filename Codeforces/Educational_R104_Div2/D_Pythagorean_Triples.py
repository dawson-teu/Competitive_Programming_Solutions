t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    for a in range(3, n, 2):
        if (a ** 2 - 1) // 2 + 1 <= n:
            count += 1
        else:
            break
    print(count)
