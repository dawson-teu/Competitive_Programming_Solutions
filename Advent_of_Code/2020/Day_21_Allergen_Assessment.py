ingredients_id = {}
allergen_id = {}
line = input()
allergen_counter = 0
ingredients_counter = 0
food_allergens = []
while not line == "":
    ingredients = line.split(" (")[0].split(" ")
    for ingredient in ingredients:
        if ingredient not in ingredients_id:
            ingredients_id[ingredient] = ingredients_counter
            ingredients_counter += 1
    allergens = line.split(" (contains ")[1].split(", ")
    allergens[-1] = allergens[-1][:-1]
    for allergen in allergens:
        if allergen not in allergen_id:
            allergen_id[allergen] = allergen_counter
            allergen_counter += 1
    food_allergens.append([[ingredients_id[i] for i in ingredients], [allergen_id[a] for a in allergens]])
    line = input()

allergen_to_ingredients = {}
while len(allergen_to_ingredients.keys()) < len(allergen_id.keys()):
    for allergen in allergen_id.values():
        possible_ingredients = set()
        for i in range(len(food_allergens)):
            if allergen in food_allergens[i][1]:
                if len(possible_ingredients) == 0:
                    possible_ingredients = set(food_allergens[i][0])
                    possible_ingredients = possible_ingredients.difference(allergen_to_ingredients.values())
                else:
                    food_ingredients = set(food_allergens[i][0]).difference(allergen_to_ingredients.values())
                    possible_ingredients = possible_ingredients.intersection(food_ingredients)
        if len(possible_ingredients) == 1:
            allergen_to_ingredients[allergen] = list(possible_ingredients)[0]

# Part 1
count = 0
for food in food_allergens:
    for ingredient in food[0]:
        if ingredient not in allergen_to_ingredients.values():
            count += 1
part_1_ans = count
print(part_1_ans)

# Part 2
ingredient_reverse_lookup = {}
for (key, value) in ingredients_id.items():
    ingredient_reverse_lookup[value] = key

allergen_reverse_lookup = {}
for (key, value) in allergen_id.items():
    allergen_reverse_lookup[value] = key

alpha_allergens = []
for allergen in allergen_to_ingredients.keys():
    alpha_allergens.append(allergen_reverse_lookup[allergen])
alpha_allergens = sorted(alpha_allergens)

deadly_ingredients = []
for allergen in alpha_allergens:
    deadly_ingredients.append(ingredient_reverse_lookup[allergen_to_ingredients[allergen_id[allergen]]])
part_2_ans = ",".join(deadly_ingredients)
print(part_2_ans)
