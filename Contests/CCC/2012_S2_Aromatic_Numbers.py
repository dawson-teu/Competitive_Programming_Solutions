roman_num = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

aromatic_number = input()
total = 0
for i in range(0, len(aromatic_number), 2):
    if i + 3 < len(aromatic_number) and roman_num[aromatic_number[i + 3]] > roman_num[aromatic_number[i + 1]]:
        total -= int(aromatic_number[i]) * roman_num[aromatic_number[i + 1]]
    else:
        total += int(aromatic_number[i]) * roman_num[aromatic_number[i + 1]]
print(total)
