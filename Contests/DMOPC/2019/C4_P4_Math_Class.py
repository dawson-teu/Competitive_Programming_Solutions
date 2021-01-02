# This is a partial solution to the problem.
import math


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


n = int(input())
a = [int(num) for num in input().split(" ")]
b = [int(num) for num in input().split(" ")]

points = []
for i in range(n):
    point = [int(num) for num in input().split(" ")]
    points.append(point)

if a[0] == b[0] and a[1] == b[1]:
    print(0)
elif n == 1:
    if dist(a, points[0]) == dist(b, points[0]):
        print(1)
    else:
        print(-1)
elif n == 2:
    if dist(a, points[0]) == dist(b, points[0]) or dist(a, points[1]) == dist(b, points[1]):
        print(1)
    elif dist(a, points[0]) == dist(b, points[1]) and dist(points[0], points[1]) / 2 == dist(a, points[0]):
        print(2)
    else:
        print(-1)
