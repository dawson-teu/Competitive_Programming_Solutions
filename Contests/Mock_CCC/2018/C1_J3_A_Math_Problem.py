import math

line = input()
k, p, x = [int(line.split(" ")[i]) for i in range(3)]

val = math.sqrt(4 * k * p * x) / (2 * x)
if math.floor(val) == 0:
    min_val = math.ceil(val) * x + (k * p) / math.ceil(val)
else:
    min_val = min(math.floor(val) * x + (k * p) / math.floor(val), math.ceil(val) * x + (k * p) / math.ceil(val))
print("{:.3f}".format(min_val))
