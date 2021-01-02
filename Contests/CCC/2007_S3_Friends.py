def bfs(start, target, graph):
    visited = [False for _ in range(10000)]
    queue = []
    dist = [-1 for _ in range(10000)]
    visited[start] = True
    queue.append(start)
    dist[start] = 0
    while len(queue) > 0:
        v = queue.pop(0)
        if v == target:
            return dist[target]
        neighbours = graph[v]
        for neighbour in neighbours:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
                dist[neighbour] = dist[v] + 1


n = int(input())
adj_list = [[] for i in range(10000)]
for i in range(n):
    line = input()
    x, y = [int(line.split(" ")[j]) for j in range(2)]
    adj_list[x].append(y)

line = input()
a, b = [int(line.split(" ")[i]) for i in range(2)]
output = []
while not a == 0 and not b == 0:
    result = bfs(a, b, adj_list)
    if result is None:
        output.append("No")
    else:
        output.append("Yes " + str(result - 1))
    line = input()
    a, b = [int(line.split(" ")[i]) for i in range(2)]

for elem in output:
    print(elem)
