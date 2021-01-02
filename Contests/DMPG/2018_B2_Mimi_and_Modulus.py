line = input()
n, m = [int(line.split(" ")[i]) for i in range(2)]
if n >= m:
    print(m - 1)
else:
    print(n % m)
