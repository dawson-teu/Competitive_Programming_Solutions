def points(suit):
    suit = suit.replace(" ", "")
    total = 0
    if len(suit) == 0:
        total += 3
    elif len(suit) == 1:
        total += 2
    elif len(suit) == 2:
        total += 1
    for char in suit:
        if char == "A":
            total += 4
        elif char == "K":
            total += 3
        elif char == "Q":
            total += 2
        elif char == "J":
            total += 1
    return total


line = input()
clubs_index = line.index("C")
diamonds_index = line.index("D")
hearts_index = line.index("H")
spades_index = line.index("S")

clubs = "".join([" " + char for char in line[clubs_index + 1:diamonds_index]])
diamonds = "".join([" " + char for char in line[diamonds_index + 1:hearts_index]])
hearts = "".join([" " + char for char in line[hearts_index + 1:spades_index]])
spades = "".join([" " + char for char in line[spades_index + 1:]])

clubs_spacing = (35 - len(clubs) - len(str(points(clubs))))
diamonds_spacing = (32 - len(diamonds) - len(str(points(diamonds))))
hearts_spacing = (34 - len(hearts) - len(str(points(hearts))))
spades_spacing = (34 - len(spades) - len(str(points(spades))))

print("Cards Dealt                       Points")
print("Clubs" + clubs + " " * clubs_spacing + str(points(clubs)))
print("Diamonds" + diamonds + " " * diamonds_spacing + str(points(diamonds)))
print("Hearts" + hearts + " " * hearts_spacing + str(points(hearts)))
print("Spades" + spades + " " * spades_spacing + str(points(spades)))

total_points = points(clubs) + points(diamonds) + points(hearts) + points(spades)
print((34 - len(str(total_points))) * " " + "Total " + str(total_points))
