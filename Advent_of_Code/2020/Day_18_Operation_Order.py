def evaluate_expression(exp, op_pref=None):
    # transform infix expression to postfix/reverse polish notation
    op_stack = []
    rev_pol_not = ""
    for char in exp:
        if char == " ":
            continue
        elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            rev_pol_not += char
        elif char in ["+", "*"]:
            if op_pref and len(op_stack) > 0:
                char_op_pref = op_pref.index(char)
                stack_op_pref = op_pref.index(op_stack[-1])
                condition = stack_op_pref <= char_op_pref
            else:
                condition = True
            while len(op_stack) > 0 and condition and not op_stack[-1] == "(":
                rev_pol_not += op_stack.pop(-1)
                if op_pref and len(op_stack) > 0:
                    char_op_pref = op_pref.index(char)
                    stack_op_pref = op_pref.index(op_stack[-1])
                    condition = stack_op_pref <= char_op_pref
                else:
                    condition = True
            op_stack.append(char)
        elif char == "(":
            op_stack.append(char)
        elif char == ")":
            while not op_stack[-1] == "(":
                rev_pol_not += op_stack.pop(-1)
            if op_stack[-1] == "(":
                op_stack.pop(-1)
    while len(op_stack) > 0:
        rev_pol_not += op_stack.pop(-1)

    # evaluate postfix/reverse polish notation with a stack
    stack = []
    for char in rev_pol_not:
        stack.append(char)
        if char in ["+", "*"]:
            op = stack.pop(-1)
            in1 = int(stack.pop(-1))
            in2 = int(stack.pop(-1))
            if op == "+":
                stack.append(in1 + in2)
            elif op == "*":
                stack.append(in1 * in2)
    return stack[0]


expressions = []
line = input()
while not line == "":
    expressions.append(line)
    line = input()

total_part_1 = 0
for expression in expressions:
    total_part_1 += evaluate_expression(expression)
part_1_ans = total_part_1
print(part_1_ans)

total_part_2 = 0
for expression in expressions:
    total_part_2 += evaluate_expression(expression, ["+", "*", "(", ")"])
part_2_ans = total_part_2
print(part_2_ans)
