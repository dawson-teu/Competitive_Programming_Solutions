n = int(input())
nums = input().split(" ")
if len(set(nums)) == len(nums):
    print("YES")
else:
    print("NO")
