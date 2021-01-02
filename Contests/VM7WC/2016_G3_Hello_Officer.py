def min_dist(arr):
    minimum = [0, 2 ** 64]
    for ele in arr:
        if dist[ele - 1] < minimum[1]:
            minimum = [ele, dist[ele - 1]]
    return minimum[0]


line = input()
n, m, b, q = [int(line.split(" ")[i]) for i in range(4)]

adj_list = [[] for i in range(n)]
for i in range(m):
    line = input()
    x, y, z = [int(line.split(" ")[i]) for i in range(3)]
    adj_list[x - 1].append([y, z])
    adj_list[y - 1].append([x, z])

queue = []
dist = [2 ** 64 for i in range(n)]
visited = [False for i in range(n)]
queue.append(b)
dist[b - 1] = 0
visited[b - 1] = True
while len(queue) > 0:
    vertex = min_dist(queue)
    visited[vertex - 1] = True
    queue.remove(vertex)
    for neighbour in adj_list[vertex - 1]:
        if not visited[neighbour[0] - 1]:
            if dist[vertex - 1] + neighbour[1] < dist[neighbour[0] - 1]:
                dist[neighbour[0] - 1] = dist[vertex - 1] + neighbour[1]
                queue.append(neighbour[0])

output = []
for i in range(q):
    query = int(input())
    if dist[query - 1] == 2 ** 64:
        output.append(-1)
    else:
        output.append(dist[query - 1])

for elem in output:
    print(elem)
