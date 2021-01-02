data = input().split(" ")
n = int(data[0])
d = abs(int(data[1]))

intervals = input().split(" ")
intervals = [int(intervals[i]) for i in range(n)]

best_interval = 10001
for interval in intervals:
    if d % interval == 0 and (d / interval) < best_interval:
        best_interval = d / interval

if best_interval == 10001:
    print("This is not the best time for a trip.")
else:
    print(int(best_interval))
