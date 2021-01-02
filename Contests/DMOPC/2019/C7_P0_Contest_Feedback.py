line = input()
a, b, c, d = [int(line.split(" ")[i]) for i in range(4)]

print("%.6f" % ((a + b) / 2))
print("%.6f" % ((a + c) / 2))
print("%.6f" % ((a + d) / 2))
print("%.6f" % ((b + c) / 2))
print("%.6f" % ((b + d) / 2))
print("%.6f" % ((c + d) / 2))
print("%.6f" % ((a + b + c) / 3))
print("%.6f" % ((a + b + d) / 3))
print("%.6f" % ((a + c + d) / 3))
print("%.6f" % ((b + c + d) / 3))
print("%.6f" % ((a + b + c + d) / 4))
