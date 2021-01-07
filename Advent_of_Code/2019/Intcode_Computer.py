def intcode_comp(program):
    memory = program.split(",")
    memory = [int(value) for value in memory]
    instruction_pointer = 0
    while True:
        op_code = memory[instruction_pointer]
        if op_code == 1 or op_code == 2:
            in_1_pos = memory[instruction_pointer + 1]
            in_2_pos = memory[instruction_pointer + 2]
            out_pos = memory[instruction_pointer + 3]
            if op_code == 1:
                memory[out_pos] = memory[in_1_pos] + memory[in_2_pos]
            elif op_code == 2:
                memory[out_pos] = memory[in_1_pos] * memory[in_2_pos]
            instruction_pointer += 4
        if op_code == 99:
            break
    return memory
