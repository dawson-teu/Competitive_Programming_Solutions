n = int(input())
sequence = []
input_seq = input().split(" ")
for i in range(n):
    sequence.append(int(input_seq[i]))

value_dict = {}
for num in sequence:
    if num in value_dict:
        value_dict[num] += 1
    else:
        value_dict[num] = 1

maxValuesDict = [(0, -1)]
for (key, val) in value_dict.items():
    if val > maxValuesDict[-1][1]:
        maxValuesDict = [(key, val)]
    elif val == maxValuesDict[-1][1]:
        maxValuesDict.append((key, val))

maxValues = []
for value in maxValuesDict:
    maxValues.append(value[0])
maxValues.sort()

output = ""
for i in range(len(maxValues)):
    if i == len(maxValues) - 1:
        output += str(maxValues[i])
    else:
        output += str(maxValues[i]) + " "
print(output)
