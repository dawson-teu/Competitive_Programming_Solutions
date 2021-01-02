d = int(input())
e = int(input())
w = int(input())

a = round((0 if d - 100 < 0 else d - 100) * 0.25 + e * 0.15 + w * 0.2, 2)
b = round((0 if d - 250 < 0 else d - 250) * 0.45 + e * 0.35 + w * 0.25, 2)

print("Plan A costs " + str(a))
print("Plan B costs " + str(b))

if a == b:
    print("Plan A and B are the same price.")
elif a > b:
    print("Plan B is cheapest.")
else:
    print("Plan A is cheapest.")
