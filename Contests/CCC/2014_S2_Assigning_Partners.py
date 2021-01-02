n = int(input())
names1 = input().split(" ")
names2 = input().split(" ")

pairs = {}
good = True
for i in range(n):
    if names1[i] == names2[i]:
        good = False
        break
    elif not names1[i] in pairs and not names2[i] in pairs:
        pairs[names1[i]] = names2[i]
        pairs[names2[i]] = names1[i]
    elif not pairs[names1[i]] == names2[i] or not pairs[names2[i]] == names1[i]:
        good = False
        break
print("good" if good else "bad")
