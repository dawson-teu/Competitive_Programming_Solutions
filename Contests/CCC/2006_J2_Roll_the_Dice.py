n = int(input())
m = int(input())
count = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i + j == 10:
            count += 1
print("There " + ("is" if count == 1 else "are") + " " + str(count) + " " +
      ("way" if count == 1 else "ways") + " to get the sum 10.")
