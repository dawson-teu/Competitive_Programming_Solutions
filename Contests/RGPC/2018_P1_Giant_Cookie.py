line = input()
n, m = [int(line.split(" ")[i]) for i in range(2)]

if n % m == 0:
    print("yes " + str(int(n / m)))
else:
    for i in range(m + 1, n + 1):
        if n % i == 0:
            print("no " + str(i - m))
            break
