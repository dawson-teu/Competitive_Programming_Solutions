t = int(input())
for _ in range(t):
    c1, c2, c3 = input().split(" ")
    c1, c2, c3 = int(c1), int(c2), int(c3)
    a1, a2, a3, a4, a5 = input().split(" ")
    a1, a2, a3, a4, a5 = int(a1), int(a2), int(a3), int(a4), int(a5)
    if a1 > c1 or a2 > c2 or a3 > c3:
        print("NO")
        continue
    buckets = [a1, a2, a3]
    if a4 > 0 and buckets[0] < c1:
        if a4 + buckets[0] <= c1:
            buckets[0] += a4
            a4 = 0
        else:
            a4 -= c1 - buckets[0]
            buckets[0] = c1
    if a5 > 0 and buckets[1] < c2:
        if a5 + buckets[1] <= c2:
            buckets[1] += a5
            a5 = 0
        else:
            a5 -= c2 - buckets[1]
            buckets[1] = c2
    if a4 > 0 or a5 > 0:
        buckets[2] += a4 + a5
    if buckets[2] > c3:
        print("NO")
    else:
        print("YES")
