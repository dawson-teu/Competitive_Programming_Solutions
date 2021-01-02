def neighbours(pos, graph, length, width):
    neighbour_list = []
    neighbour_pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for position in neighbour_pos:
        n_pos = (pos[0] + position[0], pos[1] + position[1])
        if 0 <= n_pos[0] < length and 0 <= n_pos[1] < width and not graph[n_pos[1]][n_pos[0]] == 'X':
            neighbour_list.append(n_pos)
    return neighbour_list


def index2d_to_1d(position, length):
    return position[0] + position[1] * length


def bfs(source, graph, length, width):
    queue = []
    visited = set()
    dist = {}
    queue.append(source)
    while len(queue) > 0:
        position = queue.pop(0)
        if graph[position[1]][position[0]] == 'W':
            return dist[index2d_to_1d(position, length)]
        for neighbour in neighbours(position, graph, length, width):
            if neighbour not in visited:
                if index2d_to_1d(position, length) not in dist:
                    dist[index2d_to_1d(neighbour, length)] = 1
                else:
                    dist[index2d_to_1d(neighbour, length)] = dist[index2d_to_1d(position, length)] + 1
                visited.add(neighbour)
                queue.append(neighbour)
    return -1


output = []
t = int(input())
for num in range(t):
    l, w = [int(num) for num in input().split(" ")]
    start = 0
    matrix = []

    for i in range(w):
        line = input()
        line_arr = []
        for j in range(l):
            if line[j] == 'C':
                start = (j, i)
            line_arr.append(line[j])
        matrix.append(line_arr)

    n = bfs(start, matrix, l, w)
    if n >= 60 or n < 0:
        output.append("#notworth")
    else:
        output.append(n)

for string in output:
    print(string)
