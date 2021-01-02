n = int(input())

num_neg = 0
num_zero = 0
cards = []
for i in range(n):
    cards.append(int(input()))
    if cards[i] < 0:
        num_neg += 1
    elif cards[i] == 0:
        num_zero += 1
original_len = len(cards)

max_product = 1
while True:
    max_card = (0, 0)
    for i in range(len(cards)):
        if cards[i] >= abs(max_card[0]) or abs(cards[i]) >= abs(max_card[0]) and (num_neg >= 2 or max_product < 0):
            max_card = (cards[i], i)

    if max_card[0] == 0:
        break
    if max_card[0] < 0:
        num_neg -= 1
    max_product *= max_card[0]
    cards.pop(max_card[1])

if num_neg == 1 and original_len == 1:
    print(cards[0])
elif num_neg == 1 and original_len - 1 == num_zero:
    print(0)
elif num_zero == original_len:
    print(0)
else:
    print(max_product)
