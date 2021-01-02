n = int(input())

maxVal = -1
for i in range(n):
    x1, x2 = [int(num) for num in input().split(" ")]
    maxVal = max(maxVal, x2 - x1)
print(maxVal)
