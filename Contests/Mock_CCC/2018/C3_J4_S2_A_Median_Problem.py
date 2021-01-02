n = int(input())

nums = []
for i in range(n):
    line = input()
    nums.append([int(line.split(" ")[i]) for i in range(n)])

medians = []
for i in range(n):
    medians.append(sorted(nums[i])[n // 2])

print(sorted(medians)[n // 2])
