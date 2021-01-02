dist = int(input())
n = int(input())
strokes = [int(input()) for _ in range(n)]

dp = [-1 for i in range(dist + 1)]
dp[0] = 0
for i in range(1, dist + 1):
    minimum = 10 ** 10
    for stroke in strokes:
        if i - stroke >= 0 and 0 <= dp[i - stroke] < minimum:
            minimum = dp[i - stroke]
    if not minimum == 10 ** 10:
        dp[i] = minimum + 1
    else:
        dp[i] = -1
if dp[dist] == -1:
    print("Roberta acknowledges defeat.")
else:
    print(f"Roberta wins in {dp[dist]} strokes.")
