m = int(input())
classes = []
for i in range(m):
    x, y = map(int, input().split())
    classes.append((x, y))
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    is_overlap = False
    for j in range(m):
        right_overlap = b >= classes[j][0] and a < classes[j][1]
        left_overlap = a <= classes[j][1] and classes[j][0] < b
        all_overlap = classes[j][0] <= a and b <= classes[j][1]
        if right_overlap or left_overlap or all_overlap:
            is_overlap = True
            break
    if is_overlap:
        print("Break is Over! Stop playing games! Stop watching Youtube!")
    else:
        print(":eyy:")
