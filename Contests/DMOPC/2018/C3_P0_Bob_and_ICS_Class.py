import math

col1 = input().split(" ")
col2 = input().split(" ")
r = math.floor(math.sqrt(int(col1[0]))) == math.floor(math.sqrt(int(col2[0])))
g = math.floor(math.sqrt(int(col1[1]))) == math.floor(math.sqrt(int(col2[1])))
b = math.floor(math.sqrt(int(col1[2]))) == math.floor(math.sqrt(int(col2[2])))
if r and g and b:
    print("Dull")
else:
    print("Colourful")
