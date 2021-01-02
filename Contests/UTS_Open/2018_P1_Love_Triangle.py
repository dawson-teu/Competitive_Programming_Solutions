line = input()
n, m = [int(line.split(" ")[i]) for i in range(2)]
print(max(n * m, n + m, abs(n - m)))
