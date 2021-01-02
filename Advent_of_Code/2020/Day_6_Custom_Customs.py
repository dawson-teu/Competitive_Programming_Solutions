from string import ascii_lowercase as alpha

line = input()
part_1_group = set()
part_1_count = 0

part_2_group = []
part_2_count = 0
while not line == "0":
    if line == "":
        part_1_count += len(part_1_group)
        part_1_group = set()

        alpha_set = set([letter for letter in alpha])
        for person in part_2_group:
            alpha_set = alpha_set.difference(alpha_set.difference(set([letter for letter in person])))
        part_2_group = []
        part_2_count += len(alpha_set)
    else:
        for letter in line:
            part_1_group.add(letter)
        part_2_group.append(line)
    line = input()

print(part_1_count)
print(part_2_count)
