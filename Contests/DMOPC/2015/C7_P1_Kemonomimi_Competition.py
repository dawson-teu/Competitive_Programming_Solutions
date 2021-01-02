n = int(input())
cuteness = input().split(" ")
nums = []
max_s = -1
for i in range(n):
    index, p, s, t = input().split(" ")
    nums.append([int(index), int(p), int(s), int(t)])
    max_s = max(max_s, int(s))

for i in range(n):
    index, p, s, t = nums[i]
    if p == 10:
        print(0)
    elif 180 - (int(cuteness[int(index) - 1]) * int(t) + max_s) >= 0:
        print(10 - p)
    else:
        print("The kemonomimi are too cute!")
