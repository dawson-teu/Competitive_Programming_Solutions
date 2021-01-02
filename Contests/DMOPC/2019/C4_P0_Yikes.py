a = input()
b = input()
diff = 0
for i in range(len(a)):
    if not a[i] == b[i]:
        diff += 1
if diff == 1:
    print("LARRY IS SAVED!")
else:
    print("LARRY IS DEAD!")
