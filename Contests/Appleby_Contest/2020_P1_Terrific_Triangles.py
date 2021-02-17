t = int(input())
for i in range(t):
    s1, s2, s3 = input().split(" ")
    s1, s2, s3 = int(s1), int(s2), int(s3)
    s1, s2, s3 = sorted([s1, s2, s3])
    if s1 ** 2 + s2 ** 2 == s3 ** 2:
        print("R")
    elif s1 ** 2 + s2 ** 2 > s3 ** 2:
        print("A")
    else:
        print("O")
