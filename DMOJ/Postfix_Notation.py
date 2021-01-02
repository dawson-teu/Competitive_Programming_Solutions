expression = input().split(" ")
stack = []
for symbol in expression:
    if symbol not in ["*", "/", "+", "-", "%", "^"]:
        stack.append(float(symbol))
    else:
        b = stack.pop(len(stack) - 1)
        a = stack.pop(len(stack) - 1)
        if symbol == "*":
            stack.append(a * b)
        elif symbol == "/":
            stack.append(a / b)
        elif symbol == "+":
            stack.append(a + b)
        elif symbol == "-":
            stack.append(a - b)
        elif symbol == "%":
            stack.append(a % b)
        elif symbol == "^":
            stack.append(a ** b)
print(round(stack[0], 1))
