n = int(input())

max_time = -1
projects_time = []
projects_value = []
for i in range(n):
    line = input()
    projects_time.append(int(line.split(" ")[0]))
    projects_value.append(int(line.split(" ")[1]))
    max_time = max(max_time, int(line.split(" ")[0]))

max_projects = [0]
for i in range(max_time):
    if (i + 1) in projects_time:
        max_projects.append(max(max_projects[i], projects_value[projects_time.index(i + 1)]))
    else:
        max_projects.append(max_projects[i])

output = []
q = int(input())
for i in range(q):
    t = int(input())
    if t > max_time:
        output.append(max_projects[-1])
    else:
        output.append(max_projects[t])

for elem in output:
    print(elem)
