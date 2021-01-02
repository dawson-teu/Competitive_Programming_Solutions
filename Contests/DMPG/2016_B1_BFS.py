coin_value = [5, 10, 25, 100, 200]

money = input().split(" ")
total = 0
for i in range(5):
    total += int(money[i]) * coin_value[i]
print(total)
