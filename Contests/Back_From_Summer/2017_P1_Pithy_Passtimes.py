n = int(input())
words = input().split(" ")

total = 0
for word in words:
    if len(word) <= 10:
        total += 1
print(total)
