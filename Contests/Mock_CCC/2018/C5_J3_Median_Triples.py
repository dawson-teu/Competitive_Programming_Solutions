def median(n1, n2, n3):
    if n2 <= n1 <= n3 or n3 <= n1 <= n2:
        return n1
    elif n1 <= n2 <= n3 or n3 <= n2 <= n1:
        return n2
    elif n1 <= n3 <= n2 or n2 <= n3 <= n1:
        return n3


line = input()
n, x = [int(line.split(" ")[i]) for i in range(2)]
line = input()
a = [int(line.split(" ")[i]) for i in range(n)]

count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if median(a[i], a[j], a[k]) == x:
                count += 1
print(count)
