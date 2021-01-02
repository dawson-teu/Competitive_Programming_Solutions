k = []
for i in range(3):
    k.append(int(input()))

if min(k) == k[0] and max(k) == k[2]:
    print("Good job!")
else:
    print("Try again!")
