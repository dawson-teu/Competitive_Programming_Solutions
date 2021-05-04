def solve(h1, w1, h2, w2, cur_dp):
    if not cur_dp[h1][w1][h2][w2] == 0:
        return cur_dp[h1][w1][h2][w2]
    if h1 == w1 == h2 == w2 == 1:
        return -1

    for i in range(1, w1):
        if w1 - i >= 1 and solve(h1, i, h1, w1 - i, cur_dp) == -1:
            cur_dp[h1][w1][h2][w2] = 1
            return 1
    for i in range(1, w2):
        if w2 - i >= 1 and solve(h2, i, h2, w2 - i, cur_dp) == -1:
            cur_dp[h1][w1][h2][w2] = 1
            return 1
    for i in range(1, h1):
        if h1 - i >= 1 and solve(i, w1, h1 - i, w1, cur_dp) == -1:
            cur_dp[h1][w1][h2][w2] = 1
            return 1
    for i in range(1, h2):
        if h2 - i >= 1 and solve(i, w2, h2 - i, w2, cur_dp) == -1:
            cur_dp[h1][w1][h2][w2] = 1
            return 1

    if not h1 == 1:
        if solve(1, w1, h2, w2, cur_dp) == -1:
            cur_dp[h1][w1][h2][w2] = 1
            return 1
    if not h2 == 1:
        if solve(h1, w1, 1, w2, cur_dp) == -1:
            cur_dp[h1][w1][h2][w2] = 1
            return 1
    for i in range(1, 11):
        if w1 - i >= 1 and solve(h1, w1 - i, h2, w2, cur_dp) == -1:
            cur_dp[h1][w1][h2][w2] = 1
            return 1
    for i in range(1, 11):
        if w2 - i >= 1 and solve(h1, w1, h2, w2 - i, cur_dp) == -1:
            cur_dp[h1][w1][h2][w2] = 1
            return 1
    cur_dp[h1][w1][h2][w2] = -1
    return -1


in_h1, in_w1, in_h2, in_w2 = map(int, input().split())
dp = [[[[0 for _ in range(301)] for _ in range(3)] for _ in range(301)] for _ in range(3)]
if solve(in_h1, in_w1, in_h2, in_w2, dp) == 1:
    print("W")
else:
    print("L")
