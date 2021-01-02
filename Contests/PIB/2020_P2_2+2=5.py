def f(x):
    return x // 2 - x // 7


t = int(input())
left = 1
right = 10 ** 14 + 1
ans = -1
while left <= right:
    mid = (left + right) // 2
    val = f(7 * mid)
    if val > t:
        right = mid - 1
        ans = mid - 1
    else:
        left = mid + 1

arr = []
for i in range(7):
    result = f((ans * 7) + i)
    if result <= t:
        arr.append(ans * 7 + i)
print(max(arr))
