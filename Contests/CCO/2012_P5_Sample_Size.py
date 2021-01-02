import math


def r(num):
    if num - int(num) >= 0.5:
        return int(math.ceil(num))
    else:
        return int(math.floor(num))


n = int(input())
nums = sorted([int(input()) for i in range(n)])

for i in range(1, 101):
    good = True
    k = 0
    for j in range(len(nums)):
        if not good:
            break
        while True:
            if r(k * 100 / i) == nums[j]:
                break
            k += 1
            if (r(k * 100 / i) - nums[j]) > (100 / i):
                good = False
                break
    if good:
        print(i)
        break
