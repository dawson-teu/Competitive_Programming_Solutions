n, x = map(int, input().split())

if (n - x) % 2 == 1:
    print(-1)
else:
    alpacas = ["0" for i in range(n)]
    for i in range(0, n - x, 2):
        alpacas[i] = "1"
    print(" ".join(alpacas))
