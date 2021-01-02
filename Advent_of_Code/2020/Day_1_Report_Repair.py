nums = [int(input()) for i in range(200)]
set_nums = set(nums)

# part 1
part_1_ans = 0
for num in nums:
    if (2020 - num) in set_nums:
        part_1_ans = num * (2020 - num)
        break
print(part_1_ans)

# part 2
part_2_ans = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if (2020 - nums[i] - nums[j]) in set_nums:
            part_2_ans = nums[i] * nums[j] * (2020 - nums[i] - nums[j])
print(part_2_ans)
