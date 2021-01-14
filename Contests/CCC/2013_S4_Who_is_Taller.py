import sys


def bfs(in_adj_list, start, end):
    queue = []
    visited = [False for _ in range(len(in_adj_list))]
    queue.append(start)
    visited[start] = True
    while len(queue) > 0:
        person = queue.pop(0)
        if person == end:
            return True
        for neighbour in in_adj_list[person]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
    return False


n, m = sys.stdin.readline().split(" ")
n, m = int(n), int(m)

adj_list = [[] for _ in range(n)]
for _ in range(m):
    x, y = sys.stdin.readline().split(" ")
    x, y = int(x), int(y)
    adj_list[x - 1].append(y - 1)

p, q = sys.stdin.readline().split(" ")
p, q = int(p), int(q)
if bfs(adj_list, p - 1, q - 1):
    print("yes")
elif bfs(adj_list, q - 1, p - 1):
    print("no")
else:
    print("unknown")
