t = int(input())
for i in range(t):
    n, k = input().split(" ")
    n, k = int(n), int(k)
    if n % 2 == 0:
        print((k - 1) % n + 1)
    else:
        print(((k - 1) + (k - 1) // (n // 2)) % n + 1)
