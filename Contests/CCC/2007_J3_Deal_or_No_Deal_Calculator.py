amounts = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

n = int(input())
for i in range(n):
    index = int(input())
    amounts[index - 1] = 0

offer = int(input())
value = sum(amounts) / (10 - n)
if offer > value:
    print("deal")
else:
    print("no deal")
