t = int(input())
for i in range(t):
    n = int(input())
    nums = input().split(" ")
    nums = [int(nums[j]) for j in range(n)]
    min_num = min(nums)
    count = 0
    for j in range(n):
        if not nums[j] == min_num:
            count += 1
    print(count)
