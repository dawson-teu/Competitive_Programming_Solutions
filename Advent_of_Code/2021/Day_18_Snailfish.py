import math


def add(num1, num2):
    return "[" + num1 + "," + num2 + "]"


def reduce(num):
    cur_num = num
    while True:
        new_num = explode(cur_num)

        # if the exploded number is different, continue to the next reduction cycle
        if new_num != cur_num:
            cur_num = new_num
            continue

        # if not, try splitting the number
        new_num = split(cur_num)

        # if the number is still the same, the number is already reduced
        if new_num == cur_num:
            break
        cur_num = new_num
    return cur_num


def explode(num):
    # find the index and string representation of the first four-nested pair
    explode_pair = ""
    explode_index = -1
    depth = 0
    for in_i in range(len(num)):
        # if an opening bracket is encountered, increase the current depth
        if num[in_i] == "[":
            depth += 1

        # the elements of the first four-nested pair will have a depth of 5
        if depth >= 5:
            # build the pair string, and restart on every opening bracket, keeping track of the starting index
            # exit the loop when a closing bracket is encountered
            if num[in_i] == "[":
                explode_index = in_i
                explode_pair = num[in_i]
            elif num[in_i] == "]":
                explode_pair += num[in_i]
                break
            else:
                explode_pair += num[in_i]

        # if an closing bracket is encountered, decrease the current depth
        # this is at the end of the loop body to ensure the closing bracket will be included in the four-nested pair
        if num[in_i] == "]":
            depth -= 1

    # if a pair to explode is not found, return the string unchanged
    if explode_index == -1:
        return num

    # find the number and index of the last regular number before the pair to explode
    last_int = ""
    last_index = 0
    for in_i in range(explode_index - 1, -1, -1):
        # build the regular number as a continuous string of digits
        # if the string has already been built and a non-digit character is encountered, exit the loop
        if num[in_i].isdigit():
            last_int = num[in_i] + last_int
            last_index = in_i
        elif last_int != "":
            break

    # find the number and index of the next regular number after the pair to explode
    next_int = ""
    next_index = len(num) - 1
    for in_i in range(explode_index + len(explode_pair), len(num)):
        # build the regular number as a continuous string of digits
        # if the string has already been built and a non-digit character is encountered, exit the loop
        if num[in_i].isdigit():
            next_int += num[in_i]
            next_index = in_i
        elif next_int != "":
            break

    # extract the left and right regular numbers from the pair to explode
    left, right = explode_pair[1:-1].split(",")
    left, right = int(left), int(right)

    # build the new exploded snailfish number
    new_num = ""

    # if there is a last regular number, add the substring before it and the last number after explosion
    if last_int != "":
        new_num += num[:last_index]
        new_num += str(int(last_int) + left)

    # add the substring before the exploded pair, a 0 replacing the pair, and the substring after it
    new_num += num[last_index + len(last_int):explode_index]
    new_num += "0"
    new_num += num[explode_index + len(explode_pair):next_index - len(next_int) + 1]

    # if there is a next regular number, add the next number after explosion and the substring after it
    if next_int != "":
        new_num += str(int(next_int) + right)
        new_num += num[next_index + 1:]

    return new_num


def split(num):
    # find the number and index of the first regular number greater than 10
    cur_num = ""
    cur_index = -1
    for in_i in range(len(num)):
        # build continuous strings of digits, and restart on every non-digit character, keeping track of the index
        # if the string of digits is longer than 2 (10 has 2 digits), exit the loop
        if num[in_i].isdigit():
            cur_num += num[in_i]
            cur_index = in_i
        elif len(cur_num) >= 2:
            break
        else:
            cur_num = ""

    # if no regular number is greater than 10, return the number unchanged
    if len(cur_num) < 2:
        return num

    # replace the regular number with the pair of split numbers
    left = math.floor(int(cur_num) / 2)
    right = math.ceil(int(cur_num) / 2)
    return num[:cur_index - len(cur_num) + 1] + "[" + str(left) + "," + str(right) + "]" + num[cur_index + 1:]


def magnitude(num):
    # if the num is just a regular integer, return it as an int
    if "[" not in num:
        return int(num)

    # find the index of the lowest-level comma
    depth = 0
    comma_index = -1
    for in_i in range(1, len(num) - 1):
        if num[in_i] == "[":
            depth += 1
        elif num[in_i] == "]":
            depth -= 1

        if num[in_i] == "," and depth == 0:
            comma_index = in_i
            break

    # split the number along the comma, and calculate the magnitude recursively
    left, right = num[1:comma_index], num[comma_index + 1:-1]
    return 3 * magnitude(left) + 2 * magnitude(right)


with open("InputFiles/Day_18.txt") as f:
    snailfish_nums = []
    for line in f:
        snailfish_nums.append(line.rstrip())

total = snailfish_nums[0]
for snailfish_num in snailfish_nums[1:]:
    total = reduce(add(total, snailfish_num))
part_1_ans = magnitude(total)
print(part_1_ans)

part_2_ans = -1
for i in range(len(snailfish_nums)):
    for j in range(i + 1, len(snailfish_nums)):
        # snailfish number addition is non-commutative, so both orderings must be considered for the maximum
        total = magnitude(reduce(add(snailfish_nums[i], snailfish_nums[j])))
        part_2_ans = max(part_2_ans, total)

        total = magnitude(reduce(add(snailfish_nums[j], snailfish_nums[i])))
        part_2_ans = max(part_2_ans, total)
print(part_2_ans)
