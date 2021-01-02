global Decimal


def final_interest_value(deposit):
    global Decimal
    bank_account_value = 0
    if t >= 10 ** 15 and p <= 10:
        from decimal import Decimal
    for year in range(y):
        if bank_account_value >= 10 ** 16 + 1:
            return 10 ** 16 + 1
        bank_account_value += deposit
        if t >= 10 ** 15 and p <= 10:
            bank_account_value = int(bank_account_value * Decimal(1 + p / 100))
        else:
            bank_account_value = int(bank_account_value * (1 + p / 100))
    return bank_account_value


def binary_search():
    left = 0
    right = t
    ans = -1
    while left <= right:
        middle = left + (right - left) // 2
        if final_interest_value(middle) >= t:
            right = middle - 1
            ans = middle
        else:
            left = middle + 1
    return ans


data = [int(num) for num in input().split(" ")]
p = data[0]
y = data[1]
t = data[2]

print(binary_search())
