total = 2
prev1 = 1
prev2 = 2
cur_num = -1
while cur_num <= 4000000:
    cur_num = prev1 + prev2
    prev1 = prev2
    prev2 = cur_num

    if cur_num % 2 == 0:
        total += cur_num
print(total)
