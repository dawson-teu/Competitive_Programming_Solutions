s = input()
m = int(input())
combos = []
for i in range(m):
    combos.append(input().split(" "))
combos = sorted(combos, key=lambda x: len(x[0]), reverse=True)

index = 0
total = len(s)
while index < len(s):
    found = False
    for combo in combos:
        if s[index:index + len(combo[0])] == combo[0]:
            found = True
            total += int(combo[1])
            index += len(combo[0])
            break
    if not found:
        index += 1
print(total)
