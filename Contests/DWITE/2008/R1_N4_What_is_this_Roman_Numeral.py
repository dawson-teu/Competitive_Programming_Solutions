roman_val = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

output = []
for i in range(5):
    roman_num = input()

    pos = 0
    num = 0
    while pos < len(roman_num):
        if pos + 1 < len(roman_num) and roman_val[roman_num[pos]] < roman_val[roman_num[pos + 1]]:
            num += roman_val[roman_num[pos + 1]] - roman_val[roman_num[pos]]
            pos += 2
        else:
            num += roman_val[roman_num[pos]]
            pos += 1
    output.append(num)

for elem in output:
    print(elem)
