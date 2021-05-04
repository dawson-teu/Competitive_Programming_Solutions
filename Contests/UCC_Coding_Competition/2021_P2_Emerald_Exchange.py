n = int(input())
emeralds = map(int, input().split())
cur_sum = 0
max_sum = -1
for emerald in emeralds:
    if emerald % 2 == 1:
        max_sum = max(cur_sum, max_sum)
        cur_sum = 0
    else:
        cur_sum += emerald
max_sum = max(cur_sum, max_sum)
print(max_sum)
