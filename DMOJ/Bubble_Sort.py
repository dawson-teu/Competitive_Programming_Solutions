def bubble_sort(nums):
    output = []
    changed = True
    output.append(" ".join([str(num) for num in nums]))
    while changed:
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                changed = True
                tmp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = tmp
                output.append(" ".join([str(num) for num in nums]))
    return output


n = int(input())
line = input().split(" ")
ans = bubble_sort([int(line[i]) for i in range(n)])
for elem in ans:
    print(elem)
