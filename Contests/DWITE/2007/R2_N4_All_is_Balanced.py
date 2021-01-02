output = []
for i in range(5):
    characters = input()
    stack = []
    balanced = True
    for char in characters:
        if char in ["{", "[", "("]:
            stack.append(char)
        elif char == "}":
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop(len(stack) - 1)
            else:
                balanced = False
                break
        elif char == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop(len(stack) - 1)
            else:
                balanced = False
                break
        elif char == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop(len(stack) - 1)
            else:
                balanced = False
                break
    if balanced:
        output.append("balanced")
    else:
        output.append("not balanced")

for elem in output:
    print(elem)
