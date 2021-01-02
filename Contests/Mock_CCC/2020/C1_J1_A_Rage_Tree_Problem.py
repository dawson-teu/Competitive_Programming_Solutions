max_n = -1
min_n = 101
for i in range(4):
    n = int(input())
    if n < min_n:
        min_n = n
    if n > max_n:
        max_n = n
print(min_n)
print(max_n)
