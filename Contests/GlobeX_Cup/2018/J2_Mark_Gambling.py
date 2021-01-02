import math

n = int(input())
marks = input().split(" ")
marks = [int(marks[i]) for i in range(n)]

if n % 2 == 1:
    midpoint = sorted(marks)[math.floor(n / 2)]
else:
    midpoint = sorted(marks)[int((n / 2) - 1)]
if math.floor(midpoint) > math.floor(sum(marks) / n):
    print("Winnie should take the risk")
else:
    print("That's too risky")
