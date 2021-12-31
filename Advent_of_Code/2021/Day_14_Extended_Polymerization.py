from collections import defaultdict

with open("InputFiles/Day_14.txt") as f:
    template = f.readline().rstrip()

    insertion_rules = {}
    for line in f:
        if line == '\n':
            continue
        pair, element = line.rstrip().split(' -> ')
        insertion_rules[pair] = element

# Part 1
# Brute forcing the final polymer string to find the answer
polymer = template
for _ in range(10):
    new_polymer = ''
    for i in range(len(polymer) - 1):
        pair = polymer[i] + polymer[i + 1]
        # Only the first part of each pair (and any inserted elements) are inserted during each iteration
        # Since the pairs overlap, the second part of this pair will the first part of the next pair
        # It will be inserted in the next iteration and this staggered insertion is done to prevent double insertion
        if pair in insertion_rules:
            if i == len(polymer) - 2:
                new_polymer += polymer[i] + insertion_rules[pair] + polymer[i + 1]
            else:
                new_polymer += polymer[i] + insertion_rules[pair]
        else:
            new_polymer += polymer[i]
    polymer = new_polymer

element_quantities = defaultdict(int)
for element in polymer:
    element_quantities[element] += 1

min_quantity = 10 ** 10
max_quantity = -1
for _, quantity in element_quantities.items():
    min_quantity = min(quantity, min_quantity)
    max_quantity = max(quantity, max_quantity)
part_1_ans = max_quantity - min_quantity
print(part_1_ans)

# Part 2
# Brute forcing for this part will result in memory overflow (2^40 bytes or 1 TB)
# We realize that the actual order of the polymer string isn't important and only the actual pairs themselves matter
# This means that keeping track of how many pairs there are is enough to get the final answer
pair_quantities = defaultdict(int)
for i in range(len(template) - 1):
    pair = template[i] + template[i + 1]
    pair_quantities[pair] += 1

# To find the actual number of each element from the number of pairs we also need to keep track of
# the pairs at the start and end of the string and simulate how they change
start_pair = template[:2]
end_pair = template[-2:]
for _ in range(40):
    new_pair_quantities = pair_quantities.copy()
    for pair, quantity in pair_quantities.items():
        # When an element is inserted into a pair, that pair is removed from the polymer and two new pairs are added
        # For example, NN becomes NCN after C is inserted. The NN pair is removed and a NC and CN pairs are added
        # Similarly, if there is a certain quantity of a pair and an element is inserted into it, that quantity of
        # that pair is removed and that quantity of the two pairs formed from the first part of that pair and the
        # inserted element, and the inserted element and the second element of that pair are added
        if pair in insertion_rules:
            new_pair_quantities[pair] -= quantity
            new_pair_quantities[pair[0] + insertion_rules[pair]] += quantity
            new_pair_quantities[insertion_rules[pair] + pair[1]] += quantity
    pair_quantities = new_pair_quantities

    start_pair = start_pair[0] + insertion_rules[start_pair]
    end_pair = insertion_rules[end_pair] + end_pair[1]

# When finding the actual number of each element from the number of pairs we have to remember
# that due to the pairs overlapping each element is counted twice (except for the elements at the start and the end)
# For example, NCNBCHB has one of each of the pairs NC, CN, NB, BC, CH and HB
# Looking at just the pairs, we have 3 N, 4 C, 3 B and 2 H but looking at the string we have 2 N, 2 C, 2 B and 1 H
# From this example we see that to correct for the double counting, we have to do two things:
# First, add one to the count for the elements at the start and end of the string (from the pairs we kept track of)
# This is to account for the fact that we only count these elements once and double count the others
# Second, take the count for every element and divide it by 2 to account for the double counting
element_quantities = defaultdict(int)
for pair, quantity in pair_quantities.items():
    element_quantities[pair[0]] += quantity
    element_quantities[pair[1]] += quantity
element_quantities[start_pair[0]] += 1
element_quantities[end_pair[1]] += 1
for element, quantity in element_quantities.items():
    element_quantities[element] = quantity // 2

min_quantity = 10 ** 12
max_quantity = -1
for _, quantity in element_quantities.items():
    min_quantity = min(quantity, min_quantity)
    max_quantity = max(quantity, max_quantity)
part_2_ans = max_quantity - min_quantity
print(part_2_ans)
