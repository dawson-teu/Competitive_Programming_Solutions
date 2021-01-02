import functools


def compare(x, y):
    if int(str(x) + str(y)) > int(str(y) + str(x)):
        return -1
    elif int(str(x) + str(y)) < int(str(y) + str(x)):
        return 1
    else:
        return 0


cmp = functools.cmp_to_key(compare)

n = int(input())
nums = [int(input()) for i in range(n)]

print("".join([str(char) for char in sorted(nums, key=cmp)]))
