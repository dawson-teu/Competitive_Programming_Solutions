w = int(input())
n = int(input())
weights = [int(input()) for i in range(n)]

bridge = []
for i in range(n):
    if len(bridge) > 3:
        bridge.pop(0)
    bridge.append(weights[i])
    if sum(bridge) > w:
        print(i)
        break
if sum(bridge) < w:
    print(n)
