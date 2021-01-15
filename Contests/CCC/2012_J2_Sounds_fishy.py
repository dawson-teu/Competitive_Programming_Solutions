fish_rising = True
fish_diving = True
fish_constant = True
prev = None
for i in range(4):
    if prev:
        cur = int(input())
        if cur <= prev:
            fish_rising = False
        if cur >= prev:
            fish_diving = False
        if not cur == prev:
            fish_constant = False
        prev = cur
    else:
        prev = int(input())

if fish_rising:
    print("Fish Rising")
elif fish_diving:
    print("Fish Diving")
elif fish_constant:
    print("Fish At Constant Depth")
else:
    print("No Fish")
