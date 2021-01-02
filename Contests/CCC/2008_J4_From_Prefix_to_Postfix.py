exp = input()
output = []
while not exp == "0":
    exp = exp.split(" ")
    exp.reverse()
    stack = []
    for symbol in exp:
        if symbol in ["+", "-"]:
            a = stack.pop(len(stack) - 1)
            b = stack.pop(len(stack) - 1)
            stack.append(a + " " + b + " " + symbol)
        else:
            stack.append(symbol)
    output.append(stack[0])
    exp = input()

for elem in output:
    print(elem)
