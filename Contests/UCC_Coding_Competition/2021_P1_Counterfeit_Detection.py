digits = input()
count = 0
for i in range(len(digits)):
    if (i == len(digits) - 1 and digits[i] == "2") or (digits[i] == "2" and not digits[i + 1] == "5"):
        count += 1
print(count)
