n = int(input())
line = input()
nums = [int(line.split(" ")[i]) for i in range(n)]

total = 0
for num in nums:
    if not num == sum(nums) // n:
        total += 1
print(total)
