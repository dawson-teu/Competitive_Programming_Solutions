def dij(graph, vertices):
    queue = ["YYZ"]
    dist = {}
    for node in vertices:
        dist[node] = 10 ** 10
    dist["YYZ"] = 0
    while len(queue) > 0:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if dist[vertex] + neighbour[1] < dist[neighbour[0]]:
                dist[neighbour[0]] = dist[vertex] + neighbour[1]
                if neighbour[0] not in queue:
                    queue.append(neighbour[0])
    return dist["SEA"]


for _ in range(5):
    n = int(input())
    adj_list = {}
    nodes = set()
    for i in range(n):
        line = input()
        a, b, p = line.split(" ")
        if a in adj_list:
            adj_list[a].append([b, int(p)])
        else:
            adj_list[a] = [[b, int(p)]]

        if b in adj_list:
            adj_list[b].append([a, int(p)])
        else:
            adj_list[b] = [[a, int(p)]]
        nodes.add(a)
        nodes.add(b)
    print(dij(adj_list, nodes))
