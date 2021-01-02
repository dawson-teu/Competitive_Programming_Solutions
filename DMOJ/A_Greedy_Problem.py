line = input()
n, m = [int(line.split(" ")[i]) for i in range(2)]
prices = []
for i in range(n):
    line = input()
    p, a = [int(line.split(" ")[i]) for i in range(2)]
    prices.append([p, a])

prices.sort(key=lambda x: x[0], reverse=True)

boxes_left = m
total = 0
while boxes_left > 0:
    price = prices.pop()
    if price[1] > boxes_left:
        total += boxes_left * price[0]
        boxes_left = 0
    else:
        total += price[1] * price[0]
        boxes_left -= price[1]
print(total)
