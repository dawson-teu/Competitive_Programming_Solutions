t = int(input())
for _ in range(t):
    n = int(input())
    results = [[0 for _ in range(n)] for _ in range(n)]
    if n % 2 == 0:
        for i in range(n):
            for j in range(i + 1, n):
                if (j - i) < n // 2:
                    results[i][j] = -1
                elif (j - i) > n // 2:
                    results[i][j] = 1
                else:
                    results[i][j] = 0
    else:
        for i in range(n):
            for j in range(i + 1, n):
                if (j - i) <= n // 2:
                    results[i][j] = -1
                else:
                    results[i][j] = 1
    output = ""
    for i in range(n):
        for j in range(i + 1, n):
            output += str(results[i][j]) + " "
    print(output)
