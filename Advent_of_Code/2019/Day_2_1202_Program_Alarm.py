from Intcode_Computer import intcode_comp

with open("InputFiles/Day_2.txt") as f:
    grav_assist_program = list(f)[0]
modified_program = grav_assist_program.split(",")
modified_program[1] = "12"
modified_program[2] = "2"
output_memory = intcode_comp(",".join(modified_program))
part_1_ans = output_memory[0]
print(part_1_ans)

ans = [0, 0]
for noun in range(0, 100):
    for verb in range(0, 100):
        modified_program = grav_assist_program.split(",")
        modified_program[1] = str(noun)
        modified_program[2] = str(verb)
        output_memory = intcode_comp(",".join(modified_program))
        if output_memory[0] == 19690720:
            ans = [noun, verb]
            break
part_2_ans = ans[0] * 100 + ans[1]
print(part_2_ans)
