lookup = {
    0: "00",
    1: "25",
    2: "50",
    3: "75"
}

x = int(input())
y = int(input())

value = (x * y) // 4
remainder = (x * y) % 4

print(str(value) + "." + lookup[remainder])
