a = input()
b = input()

a_char = {}
for i in a:
    if i in a_char:
        a_char[i] += 1
    else:
        a_char[i] = 1

for i in b:
    if i in a_char:
        a_char[i] -= 1

total = 0
for (key, val) in a_char.items():
    if val > 0:
        total += val
print(total)
