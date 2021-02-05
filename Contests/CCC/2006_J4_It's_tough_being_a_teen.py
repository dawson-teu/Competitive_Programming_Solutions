import itertools

rules = [("1", "7"), ("1", "4"), ("2", "1"), ("3", "4"), ("3", "5")]
while True:
    a = input()
    b = input()
    if a == "0" and b == "0":
        break
    rules.append((a, b))

working_permutation = "-1"
for permutation in itertools.permutations(["1", "2", "3", "4", "5", "6", "7"]):
    is_valid = True
    for rule in rules:
        if permutation.index(rule[0]) > permutation.index(rule[1]):
            is_valid = False
            break
    if is_valid:
        working_permutation = permutation
        break
if working_permutation == "-1":
    print("Cannot complete these tasks. Going to bed.")
else:
    print(" ".join(working_permutation))
