# This is a partial solution to the problem.
def is_sub(s1, s2):
    index = 0
    for j in range(len(s2)):
        if index >= len(s1):
            break
        if s1[index] == s2[j]:
            index += 1
    return index == len(s1)


k = int(input())
total = 0
for i in range(k + 1):
    if is_sub('10', str(i)) and not is_sub('100', str(i)):
        total += 1
print(total)
