test_num = 1
while True:
    evenly_divisible = True
    for i in range(20):
        if not test_num % (i + 1) == 0:
            evenly_divisible = False
            break
    if evenly_divisible:
        break
    test_num += 1
print(test_num)
