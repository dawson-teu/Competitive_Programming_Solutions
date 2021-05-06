import math
n, p = map(int, input().split())
students = []
for i in range(n):
    name, ma, cs, eng = input().split()
    students.append((name, math.floor(4 * math.sqrt(int(ma)) + 3 * (int(cs) ** p) - 4 * int(eng))))
print(*max(students, key=lambda x: x[1]))
print(*min(students, key=lambda x: x[1]))
