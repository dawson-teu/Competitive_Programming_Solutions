n = int(input())

output = []
for i in range(n):
    string = input()
    stack = []
    valid = True
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop(len(stack) - 1)
            else:
                valid = False
                break
        else:
            if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                valid = False
                break
    if valid and len(stack) == 0:
        output.append("YES")
    else:
        output.append("NO")

for elem in output:
    print(elem)
