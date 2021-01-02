def will_terminate(code):
    accumulator = 0
    pointer = 0
    num_executed = [0 for _ in range(len(code))]
    while num_executed[pointer] < 1:
        ins = code[pointer][0]
        if ins == "nop":
            num_executed[pointer] += 1
            pointer += 1
        elif ins == "acc":
            num_executed[pointer] += 1
            accumulator += code[pointer][1]
            pointer += 1
        elif ins == "jmp":
            num_executed[pointer] += 1
            pointer += code[pointer][1]
        if pointer >= len(code):
            return True, accumulator
    return False, accumulator


line = input()
boot_code = []
while not line == "":
    command = line.split(" ")[0]
    value = int(line.split(" ")[1])
    boot_code.append([command, value])
    line = input()

part_1_ans = will_terminate(boot_code)
print(part_1_ans[1])

part_2_ans = -1
for i in range(len(boot_code)):
    original = boot_code[i].copy()
    if original[0] == "nop":
        boot_code[i][0] = "jmp"
    elif original[0] == "jmp":
        boot_code[i][0] = "nop"
    else:
        continue
    output = will_terminate(boot_code)
    if output[0]:
        part_2_ans = output[1]
    boot_code[i] = original
print(part_2_ans)
