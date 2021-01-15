import sys
import collections


def index(pos):
    return pos[1] * n + pos[0]


m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
grid = []
max_int = -1
for i in range(m):
    line = sys.stdin.readline().split(" ")
    arr = []
    for j in range(n):
        cur_num = int(line[j])
        arr.append(cur_num)
        max_int = max(max_int, cur_num)
    grid.append(arr)

adj_list = [[] for _ in range(max_int)]
for i in range(1, max_int + 1):
    for j in range(i, max_int + 1, i):
        if 0 < i <= n and 0 < j // i <= m:
            adj_list[j - 1].append((i - 1, j // i - 1))


visited = [False for i in range(m * n)]
visited[index((0, 0))] = True
queue = collections.deque()
queue.append((0, 0))
escape = False
while len(queue) > 0:
    v = queue.popleft()
    ver_value = grid[v[1]][v[0]]
    if v == (n - 1, m - 1):
        escape = True
    for neighbour in adj_list[ver_value - 1]:
        if not visited[index(neighbour)]:
            visited[index(neighbour)] = True
            queue.append(neighbour)
print("yes" if escape else "no")
