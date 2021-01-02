line = input()
n, k = [int(line.split(" ")[i]) for i in range(2)]
prices = []
total_d = 0
for i in range(n):
    line = input()
    p, d = [int(line.split(" ")[j]) for j in range(2)]
    total_d += p
    prices.append([p, d])

prices = sorted(prices, key=lambda x: x[0] - x[1], reverse=True)


total = 0
for i in range(k):
    total += prices[i][0] - prices[i][1]
print(total_d - total)
