n = int(input())
result = []
for i in range(n):
    s = input().lower()
    output = ""
    for char in s:
        if char == "a":
            output += "Hi! "
        elif char == "e":
            output += "Bye! "
        elif char == "i":
            output += "How are you? "
        elif char == "o":
            output += "Follow me! "
        elif char == "u":
            output += "Help! "
        elif char in "0123456789":
            output += "Yes! "
    result.append(output)

for elem in result:
    print(elem)
