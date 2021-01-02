def one_three_sum(num):
    one_three = 0
    total = 0
    for char in str(num):
        if one_three % 2 == 0:
            total += int(char)
            one_three = 1
        else:
            total += 3 * int(char)
            one_three = 0
    return str(total)


nums = [input() for i in range(3)]

print("The 1-3-sum is " + one_three_sum("9780921418" + "".join(nums)))
