cities = []

city = input().split(" ")
while not city[0] == 'Waterloo':
    cities.append([city[0], int(city[1])])
    city = input().split(" ")
cities.append([city[0], int(city[1])])

minCity = ['', 201]
for city in cities:
    if city[1] < minCity[1]:
        minCity = [city[0], city[1]]

print(minCity[0])
