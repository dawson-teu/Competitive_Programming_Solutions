line = input()
n, m = [int(line.split(" ")[i]) for i in range(2)]
line = input().split(" ")
farms = []
for i in range(n):
    farms.append(int(line[i]))
farms = sorted(farms)[m:]

print(sum(farms))
