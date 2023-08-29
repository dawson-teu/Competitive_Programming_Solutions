with open("InputFiles/Day_4.txt") as f:
    lower_bound, upper_bound = f.readline().rstrip().split("-")
    lower_bound, upper_bound = int(lower_bound), int(upper_bound)

part_1_ans = 0
for password in range(lower_bound, upper_bound + 1):
    is_valid = False
    for i in range(len(str(password)) - 1):
        left, right = int(str(password)[i]), int(str(password)[i + 1])
        # if any two adjacent digits are the same, the number is valid
        # if any two adjacent digits are decreasing, the number is invalid
        if left == right:
            is_valid = True
        elif left > right:
            is_valid = False
            break
    if is_valid:
        part_1_ans += 1
print(part_1_ans)

part_2_ans = 0
for password in range(lower_bound, upper_bound + 1):
    is_valid = False
    for i in range(len(str(password)) - 1):
        left, right = int(str(password)[i]), int(str(password)[i + 1])
        # if any two adjacent digits are the same, and the digits on both sides of the pair are different,
        # the number is valid (for pairs at the beginning or end, the digit on the other side must be different)
        # if any two adjacent digits are decreasing, the number is invalid
        if left == right:
            if i == 0 or int(str(password)[i - 1]) != left:
                if i > len(str(password)) - 3 or int(str(password)[i + 2]) != right:
                    is_valid = True
        elif left > right:
            is_valid = False
            break
    if is_valid:
        part_2_ans += 1
print(part_2_ans)
