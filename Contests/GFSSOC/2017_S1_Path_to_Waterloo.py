line = input()
n, t = [int(line.split(" ")[i]) for i in range(2)]
names = ["home"]
for i in range(n):
    names.append(input())
names.append("Waterloo GO")

adj_list = [[] for i in range(n + 2)]
for i in range(t):
    line = input().split("-")
    adj_list[names.index(line[0])].append(names.index(line[1]))
    adj_list[names.index(line[1])].append(names.index(line[0]))

visited = [False for i in range(n + 2)]
visited[0] = True
dist = [-1 for i in range(n + 2)]
dist[0] = 0
queue = [0]
ans = -1
while len(queue) > 0:
    v = queue.pop(0)
    if v == n + 1:
        ans = dist[v]
        break
    for neighbour in adj_list[v]:
        # noinspection PyTypeChecker
        if not visited[neighbour]:
            # noinspection PyTypeChecker
            visited[neighbour] = True
            # noinspection PyTypeChecker
            dist[neighbour] = dist[v] + 1
            queue.append(neighbour)
if ans == -1:
    print("RIP ACE")
else:
    print(ans)
