n = int(input())
denominations = input().split(" ")
quantities = input().split(" ")
k = int(input())

notes = {}
for i in range(n):
    notes[denominations[i]] = quantities[i]

dp = [[-1, 0] for i in range(k + 1)]
dp[0] = [0, notes.copy()]

for i in range(1, k + 1):
    minimum = [[10 ** 10, {}], -1]
    for key in notes.keys():
        if i - int(key) >= 0 and 0 <= dp[i - int(key)][0] < minimum[0][0] and int(dp[i - int(key)][1][key]) > 0:
            minimum = [dp[i - int(key)], key]
    if not minimum == [[10 ** 10, {}], -1]:
        new_notes = minimum[0][1].copy()
        new_notes[minimum[1]] = str(int(new_notes[minimum[1]]) - 1)
        dp[i] = [minimum[0][0] + 1, new_notes]
print(dp[k][0])
