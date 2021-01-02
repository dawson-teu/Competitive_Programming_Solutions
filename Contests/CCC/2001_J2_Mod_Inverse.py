x = int(input())
n = int(input())

mod_inverse = -1
for i in range(100):
    if x * i % n == 1:
        mod_inverse = i
        break

if mod_inverse == -1:
    print("No such integer exists.")
else:
    print(mod_inverse)
