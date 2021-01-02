n = int(input())
m = int(input())
adj = [input() for _ in range(n)]
noun = [input() for _ in range(m)]

output = []
for i in range(n):
    for j in range(m):
        output.append(adj[i] + " as " + noun[j])

for elem in output:
    print(elem)
