line = input()
line1 = [int(line.split(" ")[i]) for i in range(5)]
line = input()
line2 = [int(line.split(" ")[i]) for i in range(5)]

line1.remove(min(line1))
line2.remove(min(line2))

print(max(sum(line1), sum(line2)))
