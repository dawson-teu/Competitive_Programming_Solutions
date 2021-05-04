n = int(input())

fib = [1, 1]
for i in range(n - 2):
    fib.append((fib[i + 1] + fib[i]) % 2021)
a = [(i + 1) % 50 + fib[i] for i in range(n)]
queue = [0]
dist = [10 ** 9 for i in range(n)]
dist[0] = 0
visited = [False for i in range(n)]
visited[0] = True
while len(queue) > 0:
    house = queue.pop(0)
    for neighbour in [house + 1, house - 1, house + a[house], house - a[house]]:
        if 0 <= neighbour < n and not visited[neighbour]:
            dist[neighbour] = dist[house] + 1
            visited[neighbour] = True
            queue.append(neighbour)
print(dist[n - 1])
