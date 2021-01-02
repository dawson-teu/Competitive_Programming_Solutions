def neighbours(pos, graph, n_row, n_col):
    neighbour_list = []
    neighbour_positions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for position in neighbour_positions:
        n_pos = [position[0] + pos[0], position[1] + pos[1]]
        if 0 <= n_pos[1] < n_col and 0 <= n_pos[0] < n_row and not graph[n_pos[0]][n_pos[1]] == 'X':
            neighbour_list.append(n_pos)
    return neighbour_list


def index_2d_to_1d(position, num_col):
    return position[1] + position[0] * num_col


def bfs(source, target, graph, teleports, num_row, num_col):
    queue = []
    visited = set()
    queue.append(source)

    dist = {}
    min_teleport_dist = -1
    while len(queue) > 0:
        position = queue.pop(0)
        if position == target and min_teleport_dist == -1:
            return 0
        elif position == target:
            return dist[index_2d_to_1d(position, num_col)] - min_teleport_dist

        if index_2d_to_1d(position, num_col) in teleports and min_teleport_dist == -1:
            if index_2d_to_1d(position, num_col) in dist:
                min_teleport_dist = dist[index_2d_to_1d(position, num_col)]
            else:
                min_teleport_dist = 0
        for neighbour in neighbours(position, graph, num_row, num_col):
            if index_2d_to_1d(neighbour, num_col) not in visited:
                if index_2d_to_1d(position, num_col) not in dist:
                    dist[index_2d_to_1d(neighbour, num_col)] = 1
                else:
                    dist[index_2d_to_1d(neighbour, num_col)] = dist[index_2d_to_1d(position, num_col)] + 1
                visited.add(index_2d_to_1d(neighbour, num_col))
                queue.append(neighbour)


[r, c] = [int(num) for num in input().split(" ")]
start = [int(num) for num in input().split(" ")]
end = [int(num) for num in input().split(" ")]

matrix = []
for i in range(r):
    matrix.append([char for char in input()])

t = int(input())
devices = set()
for i in range(t):
    devices.add(index_2d_to_1d([int(num) for num in input().split(" ")], c))

print(bfs(start, end, matrix, devices, r, c))
