def neighbours(pos, graph):
    neighbour_list = []
    neighbour_positions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for position in neighbour_positions:
        n_pos = (position[0] + pos[0], position[1] + pos[1])
        if 0 <= n_pos[0] < 10 and 0 <= n_pos[1] < 10 and not graph[n_pos[1]][n_pos[0]] == '#':
            neighbour_list.append(n_pos)
    return neighbour_list


def index2d_to_1d(position):
    return position[0] + position[1] * 10


def bfs(source, graph):
    queue = []
    visited = []
    queue.append(source)
    dist = {}
    while len(queue) > 0:
        position = queue.pop(0)
        if graph[position[1]][position[0]] == 'X' and not position == source:
            return dist[index2d_to_1d(position)]
        for neighbour in neighbours(position, graph):
            if neighbour not in visited:
                if index2d_to_1d(position) not in dist:
                    dist[index2d_to_1d(neighbour)] = 1
                else:
                    dist[index2d_to_1d(neighbour)] = dist[index2d_to_1d(position)] + 1
                visited.append(neighbour)
                queue.append(neighbour)


for num in range(5):
    start = -1
    matrix = []
    for i in range(10):
        line = input()
        line_arr = []
        for j in range(10):
            if line[j] == 'X' and start == -1:
                start = (j, i)
            line_arr.append(line[j])
        matrix.append(line_arr)
    input()
    print(bfs(start, matrix))
