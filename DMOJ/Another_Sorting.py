def sort_key(a):
    return str(a)[-1]


n = int(input())
nums = input().split(" ")
nums = [int(nums[i]) for i in range(n)]

print(" ".join([str(num) for num in sorted(sorted(nums, reverse=True), key=sort_key)]))
