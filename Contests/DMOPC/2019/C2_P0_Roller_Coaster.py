n, h_min, h_max = [int(n) for n in input().split(" ")]
children = [int(n) for n in input().split(" ") if not n == '']
total = 0
for child in children:
    if h_min <= child <= h_max:
        total += 1
print(total)
