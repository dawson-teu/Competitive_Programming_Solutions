line = input()
n, w = [int(line.split(" ")[i]) for i in range(2)]
line = input()
nums = sorted([int(line.split(" ")[i]) for i in range(n) if int(line.split(" ")[i]) < w])

left = 0
right = n - 1
total = 0
while left < right:
    if nums[left] + nums[right] <= w:
        total += (right - left)
        left += 1
    else:
        right -= 1
print(total)
