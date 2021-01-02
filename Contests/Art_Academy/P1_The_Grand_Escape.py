def rev_hash(val):
    return (244002641 * val) % 2 ** 32


line = input().split(" ")
n, m = [int(line[i]) for i in range(2)]

nums = []
for i in range(n):
    nums.append(rev_hash(int(input())))

total = 0
nums = sorted(nums, reverse=True)
for i in range(m):
    total += nums[i]
print(total)
