import re


def split_fields(passport):
    output = []
    for word in passport.split(":"):
        if " " in word:
            output += word.split(" ")
        else:
            output.append(word)
    return output


def byr(value):
    return len(value) == 4 and 1920 <= int(value) <= 2002


def iyr(value):
    return len(value) == 4 and 2010 <= int(value) <= 2020


def eyr(value):
    return len(value) == 4 and 2020 <= int(value) <= 2030


def hgt(value):
    if value[-2:] == "cm":
        return 150 <= int(value[:-2]) <= 193
    elif value[-2:] == "in":
        return 59 <= int(value[:-2]) <= 76
    else:
        return False


def hcl(value):
    return value[0] == "#" and len(value) == 7 and bool(re.match(r'[0-9a-f]{6}', value[1:]))


def ecl(value):
    return value in "amb blu brn gry grn hzl oth".split(" ")


def pid(value):
    return len(value) == 9 and bool(re.match(r'[0-9]{9}', value))


lookup = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid
}


def check_passport_1(passport):
    fields = split_fields(passport)
    needed_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    is_valid = True
    for field in needed_fields:
        if field not in fields:
            is_valid = False
            break
    return is_valid


def check_passport_2(passport):
    fields = split_fields(passport)
    is_valid = True
    for i in range(0, len(fields), 2):
        if not fields[i] == 'cid' and not lookup[fields[i]](fields[i + 1]):
            is_valid = False
            break
    return check_passport_1(passport) and is_valid


cur_passport = ""
line = input()
valid_1 = 0
valid_2 = 0
while not line == "0":
    if line == "":
        cur_passport = cur_passport[:-1]
        valid_1 += 1 if check_passport_1(cur_passport) else 0
        valid_2 += 1 if check_passport_2(cur_passport) else 0
        cur_passport = ""
    else:
        cur_passport += line + " "
    line = input()
cur_passport = cur_passport[:-1]
valid_1 += 1 if check_passport_1(cur_passport) else 0
valid_2 += 1 if check_passport_2(cur_passport) else 0
print(valid_1)
print(valid_2)
