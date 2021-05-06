n, k = map(int, input().split())
garbages = []
for garbage in input().split():
    garbages.append(int(garbage))
print(sum(sorted(garbages, reverse=True)[:k]))
