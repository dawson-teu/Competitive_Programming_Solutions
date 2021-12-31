def increasing_fuel_needed(in_align_pos):
    total_fuel = 0
    for in_pos in horizontal_pos:
        dist = abs(in_pos - in_align_pos)
        total_fuel += dist * (dist + 1) // 2
    return total_fuel


with open("InputFiles/Day_7.txt") as f:
    horizontal_pos = [int(num) for num in f.readline().split(',')]

# part 1
horizontal_pos = sorted(horizontal_pos)
part_1_ans = 0
# the median is the optimal aligning position, so we find the amount of fuel necessary at the median
# if there is an even number of positions, we find the fuel necessary for both medians and take the minimum
if len(horizontal_pos) % 2 == 0:
    align_pos_left = horizontal_pos[len(horizontal_pos) // 2 - 1]
    left_fuel = 0
    for pos in horizontal_pos:
        left_fuel += abs(pos - align_pos_left)

    align_pos_right = horizontal_pos[len(horizontal_pos) // 2]
    right_fuel = 0
    for pos in horizontal_pos:
        right_fuel += abs(pos - align_pos_right)

    part_1_ans = min(left_fuel, right_fuel)
else:
    align_pos = horizontal_pos[len(horizontal_pos) // 2 - 1]
    for pos in horizontal_pos:
        part_1_ans += abs(pos - align_pos)
print(part_1_ans)

# part 2
max_pos = max(horizontal_pos)

# naive search, O(n^2)
min_fuel = 10 ** 10
for align_pos in range(max_pos + 1):
    min_fuel = min(increasing_fuel_needed(align_pos), min_fuel)
part_2_ans_naive = min_fuel

# binary search, O(nlogn)
left = 0
right = max_pos + 1
part_2_ans_bin_search = -1
while left <= right:
    mid = (left + right) // 2
    left_fuel = increasing_fuel_needed(mid - 1)
    mid_fuel = increasing_fuel_needed(mid)
    right_fuel = increasing_fuel_needed(mid + 1)
    if left_fuel > mid_fuel > right_fuel:
        left = mid + 1
    elif left_fuel < mid_fuel < right_fuel:
        right = mid - 1
    else:
        part_2_ans_bin_search = mid_fuel
        break

# math, O(n)
# the total amount of fuel needed for a given aligning position x is
# f(x) = sum(i=0 to i=n) (1/2 * abs(p[i] - x)(abs(p[i] - x) + 1))
# simplifying into a piecewise definition and taking the derivative, we find that
# sum(p) = nx + 1/2 * (# of p[i] < x) - 1/2 * (# of p[i] > x)
# since the maximum magnitude of (# of p[i] < x) - (# of p[i] > x) is n if x is 0 or the max of p[i],
# nx - 1/2 * n <= sum(p) <= nx + 1/2 * n
# x - 1/2 <= sum(p) / n <= x + 1/2
# sum(p) / n - 1/2 <= x <= sum(p) / n + 1/2
# we know x, the optimal aligning position, is within 1/2 of sum(p) / n and this is simply the average (mean)
# however, since x might not be an integer, we might need to round x to get the integer value of the aligning position
# we know the rounded value will be within 1/2 of the original value, so the integer value will be within 1 of the mean
part_2_ans_math = 10 ** 10
average = round(sum(horizontal_pos) / len(horizontal_pos))
for align_pos in [average - 1, average, average + 1]:
    part_2_ans_math = min(increasing_fuel_needed(align_pos), part_2_ans_math)

assert part_2_ans_naive == part_2_ans_bin_search == part_2_ans_math
print(part_2_ans_naive)
