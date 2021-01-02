n = int(input())
k = 10 ** 9
if n % 2 == 0:
    val = (10 ** (n // 2)) if (n // 2) < 9 else 0
    ans = (2 * (val - 1) % k) % k
else:
    val = (10 ** ((n - 1) // 2)) if ((n - 1) // 2) < 9 else 0
    ans = ((11 * val % k) - 2) % k
print(ans)
