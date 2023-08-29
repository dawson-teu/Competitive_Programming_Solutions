def intcode_comp(program, inputs=()):
    memory = program.split(",")
    memory = [int(value) for value in memory]
    instruction_pointer = 0
    input_pointer = 0
    outputs = []
    while True:
        instruction = str(memory[instruction_pointer])
        param_str, op_code = instruction[:-2], int(instruction[-2:])
        if op_code == 1 or op_code == 2:
            param_mode = extract_param_mode(param_str, 3)

            in_1 = find_parameter(memory[instruction_pointer + 1], param_mode[0], memory)
            in_2 = find_parameter(memory[instruction_pointer + 2], param_mode[1], memory)
            out_pos = memory[instruction_pointer + 3]

            if op_code == 1:
                memory[out_pos] = in_1 + in_2
            elif op_code == 2:
                memory[out_pos] = in_1 * in_2

            instruction_pointer += 4

        elif op_code == 3:
            address = memory[instruction_pointer + 1]
            memory[address] = inputs[input_pointer]
            input_pointer += 1
            instruction_pointer += 2

        elif op_code == 4:
            param_mode = extract_param_mode(param_str, 1)
            in_1 = find_parameter(memory[instruction_pointer + 1], param_mode[0], memory)
            outputs.append(in_1)
            instruction_pointer += 2

        elif op_code == 5 or op_code == 6:
            param_mode = extract_param_mode(param_str, 2)

            in_1 = find_parameter(memory[instruction_pointer + 1], param_mode[0], memory)
            in_2 = find_parameter(memory[instruction_pointer + 2], param_mode[1], memory)

            if op_code == 5 and in_1 != 0:
                instruction_pointer = in_2
            elif op_code == 6 and in_1 == 0:
                instruction_pointer = in_2
            else:
                instruction_pointer += 3

        elif op_code == 7 or op_code == 8:
            param_mode = extract_param_mode(param_str, 3)

            in_1 = find_parameter(memory[instruction_pointer + 1], param_mode[0], memory)
            in_2 = find_parameter(memory[instruction_pointer + 2], param_mode[1], memory)
            out_pos = memory[instruction_pointer + 3]

            if op_code == 7:
                memory[out_pos] = 1 if in_1 < in_2 else 0
            elif op_code == 8:
                memory[out_pos] = 1 if in_1 == in_2 else 0

            instruction_pointer += 4

        elif op_code == 99:
            break

    return memory, outputs


def extract_param_mode(param_str, num_param):
    param_mode = [0 for _ in range(num_param)]
    index = 0
    for i in range(len(param_str) - 1, -1, -1):
        param_mode[index] = int(param_str[i])
        index += 1
    return param_mode


def find_parameter(param_val, param_mode, memory):
    if param_mode == 0:
        return memory[param_val]
    elif param_mode == 1:
        return param_val
