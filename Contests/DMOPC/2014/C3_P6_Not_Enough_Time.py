n, t = input().split(" ")
n, t = int(n), int(t)
dp = [[0 for _ in range(t + 1)] for _ in range(2)]
cur = 1
prev = 0
for i in range(n):
    w_p, v_p, w_a, v_a, w_g, v_g = input().split(" ")
    w_p, v_p, w_a, v_a, w_g, v_g = int(w_p), int(v_p), int(w_a), int(v_a), int(w_g), int(v_g)
    for j in range(t + 1):
        if j >= w_g:
            dp[cur][j] = max(dp[prev][j - w_p] + v_p, dp[prev][j - w_a] + v_a, dp[prev][j - w_g] + v_g, dp[prev][j])
        elif j >= w_a:
            dp[cur][j] = max(dp[prev][j - w_p] + v_p, dp[prev][j - w_a] + v_a, dp[prev][j])
        elif j >= w_p:
            dp[cur][j] = max(dp[prev][j - w_p] + v_p, dp[prev][j])
        else:
            dp[cur][j] = dp[prev][j]
    cur = 1 - cur
    prev = 1 - prev
print(dp[prev][t])
