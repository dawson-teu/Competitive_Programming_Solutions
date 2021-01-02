line = input()
n, k = [int(line.split(" ")[i]) for i in range(2)]
planets = []
for i in range(n):
    line = input()
    planets.append([line.split(" ")[0], int(line.split(" ")[1])])
