n = int(input())
day1 = input()
day2 = input()

total = 0
for i in range(n):
    if day1[i] == "C" and day2[i] == "C":
        total += 1
print(total)
