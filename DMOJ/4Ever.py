prefix_spelling = {
    3: "hundred",
    4: "thousand",
    7: "million",
    10: "billion"
}

tens_digit_spellings = {
    0: "",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

num_spellings = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}


def num_to_word(num):
    num = str(num)
    word = ""

    for i in range(4, len(num) + 1, 3):
        num_index = len(num) - i
        result = ""
        twenty = False
        if not int(num[num_index - 2]) == 0 and (num_index - 2) >= 0:
            result += num_spellings[int(num[num_index - 2])]
            result += prefix_spelling[3]
        if int(num[num_index - 1]) == 1 and (num_index - 1) >= 0:
            result += num_spellings[int(num[num_index - 1:num_index + 1])]
            twenty = True
        if not twenty and not int(num[num_index - 1]) == 0 and (num_index - 1) >= 0:
            result += tens_digit_spellings[int(num[num_index - 1])]
        if not twenty and not int(num[num_index]) == 0:
            result += num_spellings[int(num[num_index])]
        if not result == "":
            result += prefix_spelling[i]
        word = result + word

    for i in range(len(num)):
        index = len(num) - i
        if index == 1:
            word += num_spellings[int(num[i])]
        elif index == 2 and int(num[i]) == 1:
            word += num_spellings[int(num[i:])]
            break
        elif index == 2:
            word += tens_digit_spellings[int(num[i])]
        elif index == 3 and not int(num[i]) == 0:
            word += num_spellings[int(num[i])]
            word += prefix_spelling[index]
    return word


n = int(input())

val = len(num_to_word(n))
print(val)
while not val == 4:
    val = len(num_to_word(val))
    print(val)
