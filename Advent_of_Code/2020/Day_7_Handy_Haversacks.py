# part 1 functions
# using recursion, finds all the bags that could contain a specific colours
# this can be several levels deep, so recursion is used
def recur_find_num_colour(colour, pos_colours=0):
    if pos_colours == 0:
        pos_colours = set()
    output_colours = find_colour_for_bag(colour)
    for output_colour in output_colours:
        pos_colours.add(output_colour)
    for output_colour in output_colours:
        recur_find_num_colour(output_colour, pos_colours)
    return pos_colours


# finds all the bags directly containing a specific colour
def find_colour_for_bag(colour):
    bags = []
    for (key, value) in rules.items():
        for content in value:
            if colour == content[1]:
                bags.append(key)
    return bags


# part 2 functions
# using recursion, finds the number of bags needed to fulfill the rules for a specific colour
def recur_find_num_bags(colour):
    if not rules[colour]:
        return 0
    count = 0
    for bag in rules[colour]:
        count += int(bag[0]) * (recur_find_num_bags(bag[1]) + 1)
    return count


rules = {}
line = input()
while not line == "":
    rule_key = line.split(" contain ")[0]
    rule_key = rule_key.split(" ")[:-1]
    rule_key = " ".join(rule_key)
    bag_contents = line.split(" contain ")[1].split(", ")
    rule_value = []
    for needed_content in bag_contents:
        num = needed_content.split(" ")[0]
        col = " ".join(needed_content.split(" ")[1:-1])
        rule_value.append((num, col))
    if line.split(" contain ")[1] == "no other bags.":
        rules[rule_key] = []
    else:
        rules[rule_key] = rule_value
    line = input()

final_colours = recur_find_num_colour("shiny gold")
part_1_ans = len(final_colours)
print(part_1_ans)

part_2_ans = recur_find_num_bags("shiny gold")
print(part_2_ans)
