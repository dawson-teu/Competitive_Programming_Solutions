def neighbours(pos, graph, length, width):
    neighbour_list = []
    neighbour_pos = []
    if graph[pos[1]][pos[0]] == '+':
        neighbour_pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    elif graph[pos[1]][pos[0]] == '-':
        neighbour_pos = [(1, 0), (-1, 0)]
    elif graph[pos[1]][pos[0]] == '|':
        neighbour_pos = [(0, 1), (0, -1)]
    for position in neighbour_pos:
        n_pos = (pos[0] + position[0], pos[1] + position[1])
        if 0 <= n_pos[0] < length and 0 <= n_pos[1] < width and not graph[n_pos[1]][n_pos[0]] == '*':
            neighbour_list.append(n_pos)
    return neighbour_list


def index2d_to_1d(position, length):
    return position[0] + position[1] * length


def bfs(graph, length, width):
    queue = []
    visited = []
    dist = {}
    queue.append((0, 0))
    while len(queue) > 0:
        position = queue.pop(0)
        if position[0] == length - 1 and position[1] == width - 1:
            if index2d_to_1d(position, length) in dist:
                return dist[index2d_to_1d(position, length)] + 1
            else:
                return 1
        for neighbour in neighbours(position, graph, length, width):
            if neighbour not in visited:
                if index2d_to_1d(position, length) not in dist:
                    dist[index2d_to_1d(neighbour, length)] = 1
                else:
                    dist[index2d_to_1d(neighbour, length)] = dist[index2d_to_1d(position, length)] + 1
                visited.append(neighbour)
                queue.append(neighbour)
    return -1


t = int(input())

for num in range(t):
    r = int(input())
    c = int(input())
    matrix = []

    for i in range(r):
        matrix.append([char for char in input()])

    if r > 0 and c > 0:
        print(bfs(matrix, c, r))
    else:
        print(-1)
