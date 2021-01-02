data = input().split(" ")
vin = int(data[0])
rf = int(data[1])
rg = int(data[2])

print(vin * (1 + rf / rg))
