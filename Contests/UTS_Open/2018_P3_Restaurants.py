from collections import deque

line = input()
n, t, k, v = [int(line.split(" ")[i]) for i in range(4)]
restaurants = set(int(input()) for i in range(v))

count = 0
empty = deque()
numRestaurants = 0
for i in range(n):
    if i < t - 1:
        if i + 1 in restaurants:
            numRestaurants += 1
        else:
            empty.append(i + 1)
    else:
        if i + 1 in restaurants:
            numRestaurants += 1
        else:
            empty.append(i + 1)
        index = len(empty) - 1
        while numRestaurants < k and index >= 0:
            restaurants.add(empty[index])
            empty.pop()
            count += 1
            numRestaurants += 1
            index -= 1
        if i - t + 2 in restaurants:
            numRestaurants -= 1
        else:
            empty.popleft()
print(count)
