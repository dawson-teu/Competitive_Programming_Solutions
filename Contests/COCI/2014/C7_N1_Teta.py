k = int(input())
line = input()
prices = [int(line.split(" ")[i]) for i in range(k)]
x = int(input())
line = input()
menu = [int(line.split(" ")[i]) for i in range(4)]
t = int(input())
line = input()
items = [int(line.split(" ")[i]) for i in range(t)]

total = 0
menu_orders = []
for item in items:
    if item not in menu:
        total += prices[item - 1]
    elif len(menu_orders) == 0:
        menu_orders.append([item])
    else:
        max_menu = [-1, 0]
        for i in range(len(menu_orders)):
            if item not in menu_orders[i] and len(menu_orders[i]) > max_menu[0]:
                max_menu = [len(menu_orders), i]
        if max_menu[0] == -1:
            menu_orders.append([item])
        else:
            menu_orders[max_menu[1]].append(item)
for order in menu_orders:
    val = 0
    for item in order:
        val += prices[item - 1]
    total += min(val, x)

print(total)
