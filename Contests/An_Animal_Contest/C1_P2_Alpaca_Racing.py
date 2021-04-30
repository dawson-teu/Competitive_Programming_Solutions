n, d, k, x = map(int, input().split())
speeds = []
for i in range(n):
    speeds.append(int(input()))
p = int(input())

count = 0
for i in range(len(speeds)):
    while speeds[i] >= p:
        count += 1
        speeds[i] = int(speeds[i] * (100 - x) / 100)
        if count > k:
            break
    if count > k:
        break
if count > k:
    print("NO")
else:
    print("YES")
