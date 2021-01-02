def smallest_gap(string):
    position = []
    for j in range(n):
        if string[j] == "1":
            position.append(j)
    distance = []
    for j in range(len(position) - 1):
        distance.append(position[j + 1] - position[j])
    if not distance:
        return -1
    return min(distance)


def largest_gap(string):
    position = []
    for j in range(n):
        if string[j] == "1":
            position.append(j)
    distance = []
    for j in range(len(position) - 1):
        distance.append(position[j + 1] - position[j])
    maxDist = [-1, 0]
    for j in range(len(position) - 1):
        if distance[j] > maxDist[0]:
            maxDist = [distance[j], position[j]]
    return maxDist


n = int(input())
line = input()

ans = -1
new_line = line
if new_line[0] == "0" and new_line[-1] == "0":
    new_line = "1" + new_line[1:]
    new_line = new_line[:-1] + "1"
    ans = max(ans, smallest_gap(new_line))

new_line = line
if new_line[0] == "0":
    new_line = "1" + new_line[1:]
    dist, index = largest_gap(new_line)
    if dist >= 2:
        new_line = new_line[:index + dist // 2] + "1" + new_line[index + dist // 2 + 1:]
        ans = max(ans, smallest_gap(new_line))

new_line = line
if new_line[-1] == "0":
    new_line = new_line[:-1] + "1"
    dist, index = largest_gap(new_line)
    if dist >= 2:
        new_line = new_line[:index + dist // 2] + "1" + new_line[index + dist // 2 + 1:]
        ans = max(ans, smallest_gap(new_line))

new_line = line
dist, index = largest_gap(new_line)
if dist >= 3:
    new_line = new_line[:index + dist // 3] + "1" + new_line[index + dist // 3 + 1:]
    new_line = new_line[:index + dist * 2 // 3] + "1" + new_line[index + dist * 2 // 3 + 1:]
ans = max(ans, smallest_gap(new_line))

new_line = line
dist, index = largest_gap(new_line)
if dist >= 2:
    new_line = new_line[:index + dist // 2] + "1" + new_line[index + dist // 2 + 1:]
    dist, index = largest_gap(new_line)
    if dist >= 2:
        new_line = new_line[:index + dist // 2] + "1" + new_line[index + dist // 2 + 1:]
    ans = max(ans, smallest_gap(new_line))
print(ans)
