nums = [int(input()) for i in range(9)]

val = sum(nums) - 100
ans = [0, 0]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == val:
            ans = [i, j]
            break

for i in range(len(nums)):
    if i not in ans:
        print(nums[i])
