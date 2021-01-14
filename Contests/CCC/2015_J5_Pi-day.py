memo = {}


def num_ways_pie(min_size, n, k):
    if n == k:
        return 1
    elif k == 1:
        return 1
    elif (min_size, n, k) in memo:
        return memo[(min_size, n, k)]
    else:
        total = 0
        for i in range(min_size, n // k + 1):
            total += num_ways_pie(i, n - i, k - 1)
        memo[(min_size, n, k)] = total
        return total


in_n = int(input())
in_k = int(input())
print(num_ways_pie(1, in_n, in_k))
