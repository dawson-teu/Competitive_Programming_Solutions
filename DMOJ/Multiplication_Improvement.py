s = input().split("x")
print("x".join([str(num) for num in sorted([int(num) for num in s])]))

total = 1
for num in [int(num) for num in s]:
    total *= num
print(total)
