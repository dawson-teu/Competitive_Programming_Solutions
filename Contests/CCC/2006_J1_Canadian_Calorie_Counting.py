burger = [461, 431, 420, 0]
side = [100, 57, 70, 0]
drink = [130, 160, 118, 0]
dessert = [167, 266, 75, 0]
total_arr = [burger, side, drink, dessert]

total = 0
for i in range(4):
    choice = int(input())
    total += total_arr[i][choice - 1]
print("Your total Calorie count is " + str(total) + ".")
