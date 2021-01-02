quarters = int(input())
n = [int(input()) for i in range(3)]

total = 0
machine = 0
while quarters > 0:
    n[machine] += 1
    if n[machine] >= 35 and machine == 0:
        quarters += 30
        n[machine] = 0
    elif n[machine] >= 100 and machine == 1:
        quarters += 60
        n[machine] = 0
    elif n[machine] >= 10 and machine == 2:
        quarters += 9
        n[machine] = 0
    total += 1
    machine += 1
    machine %= 3
    quarters -= 1
print(f'Martha plays {total} times before going broke.')
