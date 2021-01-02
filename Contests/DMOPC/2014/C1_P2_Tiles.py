dim = input().split(" ")
w = int(dim[0])
h = int(dim[1])

tile = int(input())
print((w // tile) * (h // tile))
