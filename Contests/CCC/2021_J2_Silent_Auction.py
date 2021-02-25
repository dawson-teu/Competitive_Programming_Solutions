n = int(input())
max_bid = (-1, "")
for i in range(n):
    name = input()
    bid = int(input())
    if bid > max_bid[0]:
        max_bid = (bid, name)
print(max_bid[1])
