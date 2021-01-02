from string import ascii_uppercase as alpha


def neighbours(point):
    neighbour_pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbour_list = []
    for pos in neighbour_pos:
        if 0 <= point[1] + pos[1] < len(matrix) and 0 <= point[0] + pos[0] < len(matrix[0]) and \
                not matrix[point[1] + pos[1]][point[0] + pos[0]] == "#":
            neighbour_list.append((point[0] + pos[0], point[1] + pos[1]))
    return neighbour_list


def index2d_to_1d(position):
    return position[0] + position[1] * len(matrix[0])


def bfs(start, target):
    dist = {}
    visited = set()
    queue = [start]
    while len(queue) > 0:
        point = queue.pop(0)
        if point == target:
            return dist[index2d_to_1d(point)]
        for neighbour in neighbours(point):
            if neighbour not in visited:
                if index2d_to_1d(point) not in dist:
                    dist[index2d_to_1d(neighbour)] = 1
                else:
                    dist[index2d_to_1d(neighbour)] = dist[index2d_to_1d(point)] + 1
                visited.add(neighbour)
                queue.append(neighbour)


matrix = []
points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    line = input()
    line_arr = [char for char in line]
    matrix.append(line_arr)
    for letter in alpha[:12]:
        if letter in line_arr:
            points[alpha.index(letter)] = (line_arr.index(letter), i)

point_dist = {}
for i in range(12):
    for j in range(i, 12):
        if i == j:
            point_dist[alpha[i] + alpha[j]] = 0
        else:
            result = bfs(points[i], points[j])
            point_dist[alpha[i] + alpha[j]] = result
            point_dist[alpha[j] + alpha[i]] = result

output = []
for i in range(5):
    query = input()
    if len(query) == 1:
        output.append(0)
    else:
        total = 0
        for j in range(len(query) - 1):
            total += point_dist[query[j] + query[j + 1]]
        output.append(total)

for elem in output:
    print(elem)
