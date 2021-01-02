n = int(input())
nums = input().split(" ")

nums = sorted(nums)
ans = 10 ** 10
for i in range(n - 1):
    ans = min(ans, abs(int(nums[i + 1]) - int(nums[i])))
print(ans)
