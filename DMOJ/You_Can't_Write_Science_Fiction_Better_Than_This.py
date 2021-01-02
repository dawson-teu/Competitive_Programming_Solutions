def neighbours(vertex, graph):
    return graph[vertex]


def bfs(start, target, graph):
    if start == target:
        return 0

    queue = []
    visited = set()
    dist = {}
    queue.append(start)
    while len(queue) > 0:
        vertex = queue.pop(0)
        if vertex == target:
            return dist[vertex]
        for neighbour in neighbours(vertex, graph):
            if neighbour not in visited:
                if vertex not in dist:
                    dist[neighbour] = 1
                else:
                    dist[neighbour] = dist[vertex] + 1
                visited.add(neighbour)
                queue.append(neighbour)
    return -1


data = input().split(' ')
data_arr = []
for num in data:
    data_arr.append(num)
n = int(data[0])
m = int(data[1])
a = int(data[2])
b = int(data[3])

edges = {}
for i in range(m):
    edge = [int(num) for num in input().split(' ')]
    if edge[0] not in edges:
        edges[edge[0]] = [edge[1]]
    else:
        edges[edge[0]].append(edge[1])

    if edge[1] not in edges:
        edges[edge[1]] = [edge[0]]
    else:
        edges[edge[1]].append(edge[0])

firstDist = bfs(1, a, edges)
secondDist = bfs(a, b, edges)
if firstDist == -1 or secondDist == -1:
    print(-1)
else:
    print(firstDist + secondDist)
