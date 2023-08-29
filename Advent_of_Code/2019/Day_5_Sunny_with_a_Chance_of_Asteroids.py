from Intcode_Computer import intcode_comp

with open("InputFiles/Day_5.txt") as f:
    test_diagnostic_program = list(f)[0]

_, outputs = intcode_comp(test_diagnostic_program, [1])
part_1_ans = outputs[-1]
print(part_1_ans)

_, outputs = intcode_comp(test_diagnostic_program, [5])
part_2_ans = outputs[0]
print(part_2_ans)
