def score_game(deck):
    total_score = 0
    for i in range(len(deck), 0, -1):
        total_score += i * deck[len(deck) - i]
    return total_score


def recur_combat(player_deck_1, player_deck_2):
    prev_decks = set()
    deck_1 = player_deck_1
    deck_2 = player_deck_2
    while len(deck_1) > 0 and len(deck_2) > 0:
        prev_decks.add((tuple(deck_1), tuple(deck_2)))
        if deck_1[0] <= len(deck_1) - 1 and deck_2[0] <= len(deck_2) - 1:
            result = recur_combat(deck_1[1:deck_1[0] + 1], deck_2[1: deck_2[0] + 1])
            if result[1] == 1:
                deck_1.append(deck_1.pop(0))
                deck_1.append(deck_2.pop(0))
            elif result[1] == 2:
                deck_2.append(deck_2.pop(0))
                deck_2.append(deck_1.pop(0))
        elif deck_1[0] > deck_2[0]:
            deck_1.append(deck_1.pop(0))
            deck_1.append(deck_2.pop(0))
        elif deck_1[0] < deck_2[0]:
            deck_2.append(deck_2.pop(0))
            deck_2.append(deck_1.pop(0))
        if (tuple(deck_1), tuple(deck_2)) in prev_decks:
            return deck_1.copy(), 1
    if len(deck_1) == 0:
        return deck_2.copy(), 2
    else:
        return deck_1.copy(), 1


input()  # Clear line containing "Player 1:"
player_1_deck = []
line = input()
while not line == "":
    player_1_deck.append(int(line))
    line = input()

input()  # Clear line containing "Player 2:"
player_2_deck = []
line = input()
while not line == "":
    player_2_deck.append(int(line))
    line = input()

deck_1_part_one = player_1_deck.copy()
deck_2_part_one = player_2_deck.copy()
while len(deck_1_part_one) > 0 and len(deck_2_part_one) > 0:
    if deck_1_part_one[0] > deck_2_part_one[0]:
        deck_1_part_one.append(deck_1_part_one.pop(0))
        deck_1_part_one.append(deck_2_part_one.pop(0))
    elif deck_1_part_one[0] < deck_2_part_one[0]:
        deck_2_part_one.append(deck_2_part_one.pop(0))
        deck_2_part_one.append(deck_1_part_one.pop(0))

winning_deck = []
if len(deck_1_part_one) == 0:
    winning_deck = deck_2_part_one.copy()
    winner = 2
else:
    winning_deck = deck_1_part_one.copy()
    winner = 1

part_1_ans = score_game(winning_deck)
print(part_1_ans, winner)

(winning_deck, winner) = recur_combat(player_1_deck, player_2_deck)
part_2_ans = score_game(winning_deck)
print(part_2_ans, winner)
