def neighbours(pos):
    neighbour_list = []
    neighbour_pos = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    for position in neighbour_pos:
        n_pos = [pos[0] + position[0], pos[1] + position[1]]
        if 0 <= n_pos[0] < 8 and 0 <= n_pos[1] < 8:
            neighbour_list.append(n_pos)
    return neighbour_list


def index2d_to_1d(position):
    return position[0] + position[1] * 8


def bfs(source, target):
    queue = []
    visited = []
    dist = {}
    queue.append(source)
    while len(queue) > 0:
        position = queue.pop(0)
        if position == target:
            if index2d_to_1d(position) in dist:
                return dist[index2d_to_1d(target)]
            else:
                return 0
        for neighbour in neighbours(position):
            if neighbour not in visited:
                if index2d_to_1d(position) not in dist:
                    dist[index2d_to_1d(neighbour)] = 1
                else:
                    dist[index2d_to_1d(neighbour)] = dist[index2d_to_1d(position)] + 1
                visited.append(neighbour)
                queue.append(neighbour)
    return -1


start = [int(num) - 1 for num in input().split(' ')]
end = [int(num) - 1 for num in input().split(' ')]
print(bfs(start, end))
