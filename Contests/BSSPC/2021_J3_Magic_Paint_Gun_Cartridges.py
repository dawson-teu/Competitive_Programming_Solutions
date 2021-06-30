m, n = map(int, input().split())
red_needed = [[0 for _ in range(m)] for _ in range(n)]
yellow_needed = [[0 for _ in range(m)] for _ in range(n)]
blue_needed = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(m):
        if line[j] in ["R", "O", "P", "B"]:
            red_needed[i][j] += 1
        if line[j] in ["Y", "O", "G", "B"]:
            yellow_needed[i][j] += 1
        if line[j] in ["U", "G", "P", "B"]:
            blue_needed[i][j] += 1
red = 0
yellow = 0
blue = 0
for i in range(n):
    for j in range(m):
        if red_needed[i][j] == 1 and (j == 0 or not red_needed[i][j - 1] == 1):
            red += 1
        if yellow_needed[i][j] == 1 and (j == 0 or not yellow_needed[i][j - 1] == 1):
            yellow += 1
        if blue_needed[i][j] == 1 and (j == 0 or not blue_needed[i][j - 1] == 1):
            blue += 1
print(red, yellow, blue)
