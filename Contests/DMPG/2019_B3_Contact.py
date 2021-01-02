line = input()
k = int(input())
total = 0
spam = False
for char in line:
    if char == "S":
        total += 1
    if char == "R":
        total = 0
    if total >= k:
        spam = True
if spam:
    print("Spamming")
else:
    print("All good")
