def x_gcd(a, b):
    x = 0
    y = 1
    z = b
    prev_x = 1
    prev_y = 0
    prev_z = a
    while not z == 0:
        q = prev_z // z
        [prev_z, z] = (z, prev_z - q * z)
        [prev_x, x] = (x, prev_x - q * x)
        [prev_y, y] = (y, prev_y - q * y)
    return prev_x


line = input()
n, m = [int(line.split(" ")[i]) for i in range(2)]
print(x_gcd(n, m) % m)
