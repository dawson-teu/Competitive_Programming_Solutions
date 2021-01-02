output = []
for _ in range(5):
    def neighbours(p):
        neighbourPos = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, 1], [-1, 0], [-1, 1]]
        neighbourList = []
        for neigh in neighbourPos:
            newPos = [p[0] + neigh[0], p[1] + neigh[1]]
            if 0 <= newPos[0] < 8 and 0 <= newPos[1] < 8 and not grid[newPos[1]][newPos[0]] == "#":
                neighbourList.append(newPos)
        return neighbourList


    def index2d(p):
        return 8 * p[1] + p[0]


    posA = [-1, -1]
    posB = [-1, -1]
    grid = []
    for i in range(8):
        line = input()
        lineArr = []
        for j in range(8):
            if line[j] == "A":
                posA = [j, i]
            if line[j] == "B":
                posB = [j, i]
            lineArr.append(line[j])
        grid.append(lineArr)

    visited = [False for i in range(8 * 8)]
    dist = [-1 for i in range(8 * 8)]
    queue = [posA]
    visited[index2d(posA)] = True
    dist[index2d(posA)] = 0
    while len(queue) > 0:
        pos = queue.pop(0)
        if pos == posB:
            output.append(dist[index2d(pos)])
        for n in neighbours(pos):
            if not visited[index2d(n)]:
                visited[index2d(n)] = True
                dist[index2d(n)] = dist[index2d(pos)] + 1
                queue.append(n)

for elem in output:
    print(elem)
