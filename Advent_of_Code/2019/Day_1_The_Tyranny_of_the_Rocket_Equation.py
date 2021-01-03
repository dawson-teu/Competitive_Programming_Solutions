total_1 = 0
total_2 = 0

f = open("InputFiles/Day_1.txt", "r")
for i in range(100):
    num = int(f.readline())

    total_1 += (num // 3) - 2
    while (num // 3 - 2) > 0:
        num //= 3
        num -= 2
        total_2 += num
f.close()

print(total_1)  # part 1
print(total_2)  # part 2
