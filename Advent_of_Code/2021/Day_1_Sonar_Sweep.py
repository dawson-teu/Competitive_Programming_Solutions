with open("InputFiles/Day_1.txt") as f:
    measurements = []
    for line in f:
        measurements.append(int(line))

part_1_ans = 0
for i in range(1, len(measurements)):
    if measurements[i] > measurements[i - 1]:
        part_1_ans += 1
print(part_1_ans)

part_2_ans = 0
for i in range(3, len(measurements)):
    # If any four numbers are A, B, C, D, the two windows they form have sums of A + B + C and B + C + D
    # An increase means B + C + D > A + B + C and cancelling out B and C gives D > A (the condition in the code)
    # This can also be thought of as the last number in the previous window leaving the window (4 numbers back)
    # and the current number joining the window, so the window sum to increase current must be > than the last
    if measurements[i] > measurements[i - 3]:
        part_2_ans += 1
print(part_2_ans)
