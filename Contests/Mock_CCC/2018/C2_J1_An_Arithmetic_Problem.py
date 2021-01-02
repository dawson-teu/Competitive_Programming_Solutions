data = input()
n1 = int(data.split(" + ")[0])
n2 = int(data.split(" + ")[1].split(" = ")[0])
a = int(data.split(" + ")[1].split(" = ")[1])

print(n1 + n2 == a)
