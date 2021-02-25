n = int(input())
line = input().split(" ")
heights = [int(line[i]) for i in range(n + 1)]
line = input().split(" ")
widths = [int(line[i]) for i in range(n)]
total_area = 0
for i in range(n):
    total_area += 1/2 * widths[i] * (heights[i] + heights[i + 1])
print(total_area)
