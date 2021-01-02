def bfs(graph):
    queue = [1]
    visited = set()
    while len(queue) > 0:
        vertex = queue.pop(0)
        if vertex == n:
            return True
        if vertex in graph:
            for neighbour in graph[vertex]:
                if neighbour[0] not in visited:
                    queue.append(neighbour[0])
                    visited.add(neighbour[0])
    return False


data = input().split(" ")
n = int(data[0])
m = int(data[1])

adj_list = {}
for i in range(m):
    edge = input().split(" ")
    s = int(edge[0])
    t = int(edge[1])
    if s in adj_list:
        adj_list[s].append((t, i))
    else:
        adj_list[s] = [(t, i)]

result = {}
for (key, val) in adj_list.items():
    for i in range(len(val)):
        new_adj_list = adj_list.copy()
        new_adj_list[key] = adj_list[key][:i] + adj_list[key][i + 1:]
        result[adj_list[key][i][1]] = bfs(new_adj_list)

for i in range(m):
    print("YES" if result[i] else "NO")
