low_cards = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]


def next_n_cards_low(in_deck, n, index):
    if 52 - index - 1 < n:
        return False
    else:
        low = True
        for j in range(index + 1, index + n + 1):
            if in_deck[j] not in low_cards:
                low = False
                break
        return low


deck = []
for i in range(52):
    deck.append(input())

player1 = True
score1 = 0
score2 = 0
for i in range(52):
    player_num = "A" if player1 else "B"
    scored_points = -1
    if deck[i] == "ace" and next_n_cards_low(deck, 4, i):
        scored_points = 4
    elif deck[i] == "king" and next_n_cards_low(deck, 3, i):
        scored_points = 3
    elif deck[i] == "queen" and next_n_cards_low(deck, 2, i):
        scored_points = 2
    elif deck[i] == "jack" and next_n_cards_low(deck, 1, i):
        scored_points = 1
    if not scored_points == -1:
        print("Player " + player_num + " scores " + str(scored_points) + " point(s).")
        if player1:
            score1 += scored_points
        else:
            score2 += scored_points
    player1 = not player1
print("Player A: " + str(score1) + " point(s).")
print("Player B: " + str(score2) + " point(s).")
