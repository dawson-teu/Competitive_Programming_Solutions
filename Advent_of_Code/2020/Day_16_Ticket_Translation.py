def condition(val, a, b, c, d):
    # returns whether the value is in either range: (a-b) and (c-d)
    return not a <= val <= b and not c <= val <= d


rules = {}
line = input()
while not line == "":
    field_name = line.split(": ")[0]
    range_1 = line.split(": ")[1].split(" or ")[0]
    range_2 = line.split(": ")[1].split(" or ")[1]
    range_1 = [int(num) for num in range_1.split("-")]
    range_2 = [int(num) for num in range_2.split("-")]
    rules[field_name] = [range_1, range_2]
    line = input()

input()  # clear line containing "your ticket:"
line = input()
my_ticket = [int(num) for num in line.split(",")]

input()  # clear blank line
input()  # clear line containing "nearby tickets:"
nearby_tickets = []
line = input()
while not line == "":
    nearby_tickets.append([int(i) for i in line.split(",")])
    line = input()

# part 1
valid_values = set()
for (key, value) in rules.items():
    for i in range(value[0][0], value[0][1] + 1):
        valid_values.add(i)
    for i in range(value[1][0], value[1][1] + 1):
        valid_values.add(i)

total = 0
for ticket in nearby_tickets:
    for value in ticket:
        if value not in valid_values:
            total += value
part_1_ans = total
print(part_1_ans)

# part 2
valid_tickets = []
for ticket in nearby_tickets:
    is_ticket_valid = True
    for value in ticket:
        if value not in valid_values:
            is_ticket_valid = False
            break
    if is_ticket_valid:
        valid_tickets.append(ticket)

ticket_fields = ["" for _ in range(len(my_ticket))]
available_ticket_fields = [field for field in rules.keys()]

while len(available_ticket_fields) > 0:
    ticket_possible_fields = []
    for i in range(len(my_ticket)):
        possible_fields = []
        for field in available_ticket_fields:
            is_field_possible = True
            for j in range(len(valid_tickets)):
                lower_left = rules[field][0][0]  # the left side of the lower range
                lower_right = rules[field][0][1]  # the right side of the lower range
                upper_left = rules[field][1][0]  # the left side of the upper range
                upper_right = rules[field][1][1]  # the right side of the lower range
                if condition(valid_tickets[j][i], lower_left, lower_right, upper_left, upper_right):
                    is_field_possible = False
                    break
            if is_field_possible:
                possible_fields.append(field)
        ticket_possible_fields.append(possible_fields)

    for i in range(len(ticket_possible_fields)):
        if len(ticket_possible_fields[i]) == 1:
            valid_field = ticket_possible_fields[i][0]
            ticket_fields[i] = valid_field
            available_ticket_fields.remove(valid_field)
            break

product = 1
for i in range(len(ticket_fields)):
    if ticket_fields[i].startswith("departure"):
        product *= my_ticket[i]
part_2_ans = product
print(part_2_ans)
