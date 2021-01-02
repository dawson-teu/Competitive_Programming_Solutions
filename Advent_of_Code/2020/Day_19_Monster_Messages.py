import re


def find_rule(n, rule_dict, calling_n="0", num_recursion=0):
    continue_recursion = True
    if n == calling_n and num_recursion > 20:
        continue_recursion = False
    if rule_dict[n].count("|") == 0 and rule_dict[n].count(" ") == 0 and rule_dict[n].isalpha():
        return rule_dict[n]
    output = "("
    or_used = False
    for char in rule_dict[n].split(" "):
        if char == "|":
            output += ")" + char + "("
            or_used = True
        elif continue_recursion:
            output += find_rule(char, rule_dict, n, (num_recursion + 1 if n == calling_n else num_recursion))
    if or_used:
        return "(" + output + "))"
    return output + ")"


rules = {}
line = input()
while not line == "":
    val = line.split(": ")[1]
    val = val.replace("\"", "")
    rules[line.split(":")[0]] = val
    line = input()

messages = []
line = input()
while not line == "":
    messages.append(line)
    line = input()

# Part 1
regex_rule = re.compile(find_rule("0", rules))
count = 0
for message in messages:
    if regex_rule.fullmatch(message):
        count += 1
part_1_ans = count
print(part_1_ans)

# Part 2
rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"
regex_rule = re.compile(find_rule("0", rules))
count = 0
for message in messages:
    if regex_rule.fullmatch(message):
        count += 1
part_2_ans = count
print(part_2_ans)
