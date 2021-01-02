valid_1 = 0
valid_2 = 0
for i in range(1000):
    line = input()
    num1 = int(line.split(" ")[0].split("-")[0])
    num2 = int(line.split(" ")[0].split("-")[1])
    letter = line.split(" ")[1][:1]
    password = line.split(" ")[2]

    # part 1
    if num1 <= int(password.count(letter)) <= num2:
        valid_1 += 1

    # part 2
    if (password[num1 - 1] == letter) ^ (password[num2 - 1] == letter):
        valid_2 += 1

print(valid_1)
print(valid_2)
