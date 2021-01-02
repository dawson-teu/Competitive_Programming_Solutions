n = int(input())
output = []
index1 = 1
index2 = n
while index1 <= index2:
    output.append(str(index1))
    if not index1 == index2:
        output.append(str(index2))
    index1 += 1
    index2 -= 1
print(" ".join(output))
