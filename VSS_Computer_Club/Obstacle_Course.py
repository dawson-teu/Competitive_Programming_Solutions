line = input()
num_obstacles, removed_obstacles, speed = [int(num) for num in line.split(" ")]

# using code (linear time)
time_lap = (4 * 300) / speed
time = 0
for i in range(num_obstacles, -1, -removed_obstacles):
    time += time_lap
    time += i * 2
ans = int(time)
print(ans)

# using math (constant time)
# finds the time taken for every lap, not counting the obstacles
ans = (num_obstacles // removed_obstacles + 1) * (4 * 300 / speed)
# adds in the time taken for the obstacles using the sum of an arithmetic series
ans += 1/2 * 2 * (num_obstacles // removed_obstacles + 1) * (num_obstacles + num_obstacles % removed_obstacles)
ans = int(ans)
print(ans)
