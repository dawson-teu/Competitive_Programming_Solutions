preamble_length = 25


def is_valid_num(num, valid_nums):
    valid_nums_set = set(valid_nums)
    for valid_num in valid_nums:
        if not num == valid_num * 2 and (num - valid_num) in valid_nums_set:
            return True
    return False


message = []
line = input()
while not line == "":
    message.append(int(line))
    line = input()

# part 1
valid_numbers = message[:preamble_length]
part_1_ans = 0
for i in range(preamble_length, len(message)):
    if not is_valid_num(message[i], valid_numbers):
        part_1_ans = message[i]
        break
    valid_numbers = valid_numbers[1:] + [message[i]]
print(part_1_ans)

# part 2
prefix_sum_arr = [0]
for i in range(len(message)):
    prefix_sum_arr.append(prefix_sum_arr[i] + message[i])

sum_range = (0, 0)
flag = False
for i in range(len(message)):
    if flag:
        break
    for j in range(i + 1, len(message)):
        if prefix_sum_arr[j] - prefix_sum_arr[i] == part_1_ans:
            sum_range = (i, j)
            flag = True
            break

max_range = max(message[sum_range[0]:sum_range[1]])
min_range = min(message[sum_range[0]:sum_range[1]])
part_2_ans = min_range + max_range
print(part_2_ans)
