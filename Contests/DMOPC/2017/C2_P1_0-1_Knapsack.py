n = int(input())

total = 0
for i in range(n):
    item = input().split(" ")
    if int(item[1]) > 0:
        total += int(item[0])
print(total)
