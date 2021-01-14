symbol_val = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}


def roman_num_to_int(in_roman_num):
    cur_index = 0
    total = 0
    while cur_index < len(in_roman_num):
        cur_char = in_roman_num[cur_index]
        next_char = in_roman_num[cur_index + 1] if cur_index + 1 < len(in_roman_num) else None
        if cur_char == "I" and next_char in ["V", "X"] or cur_char == "X" and next_char in ["L", "C"] or \
                cur_char == "C" and next_char in ["D", "M"]:
            total += symbol_val[next_char] - symbol_val[cur_char]
            cur_index += 2
        else:
            total += symbol_val[cur_char]
            cur_index += 1
    return total


def int_to_roman_num(in_int):
    out_roman_num = ""
    for (key, value) in sorted(list(symbol_val.items()), key=lambda x: x[1], reverse=True):
        num_symbol = in_int // value
        if num_symbol > 0:
            out_roman_num += key * num_symbol
            in_int %= value
    return out_roman_num


n = int(input())
for _ in range(n):
    line = input()
    [roman_num1, roman_num2] = line.split("+")
    roman_num2 = roman_num2.strip("=")
    output = roman_num_to_int(roman_num1) + roman_num_to_int(roman_num2)
    if output > 1000:
        print(line + "CONCORDIA CUM VERITATE")
    else:
        print(line + str(int_to_roman_num(output)))
