n = int(input())
nums = [int(input()) for i in range(n)]

dp = [0 for _ in range(n)]
for i in range(n):
    maxi = -1
    for j in range(i + 1):
        maxi = max(maxi, dp[i - j - 1] + nums[j])
    dp[i] = maxi
print(dp[-1])
