s = input()
t = input()

matching_len = -1
for i in range(min(len(s), len(t))):
    if not s[i] == t[i]:
        matching_len = i
        break
if matching_len == -1:
    matching_len = min(len(s), len(t))
print(len(s) - matching_len + len(t) - matching_len)
