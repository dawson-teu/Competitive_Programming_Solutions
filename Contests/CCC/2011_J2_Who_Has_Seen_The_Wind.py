h = int(input())
m = int(input())

t = -1
for i in range(1, m + 1):
    if (-6 * (i ** 4) + h * (i ** 3) + 2 * (i ** 2) + i) <= 0:
        t = i
        break
if t == -1:
    print("The balloon does not touch ground in the given time.")
else:
    print("The balloon first touches ground at hour: ")
    print(t)
