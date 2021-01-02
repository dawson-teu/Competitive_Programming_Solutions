n = int(input())
output = []
for i in range(n):
    a = input()
    b = input()
    c = input()
    d = a.startswith(b) or a.startswith(c) or a.endswith(b) or a.endswith(c)
    e = b.startswith(a) or b.startswith(c) or b.endswith(a) or b.endswith(c)
    f = c.startswith(a) or c.startswith(b) or c.endswith(a) or c.endswith(b)
    if d or e or f:
        output.append("No")
    else:
        output.append("Yes")

for elem in output:
    print(elem)
