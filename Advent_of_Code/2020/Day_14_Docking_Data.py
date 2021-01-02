def run_mask_part_1(value, bit_mask):
    output = ""
    for i in range(len(bit_mask)):
        if not bit_mask[i] == "X":
            output += bit_mask[i]
        else:
            output += value[i]
    return output


def run_mask_part_2(value, bit_mask):
    output = ""
    for i in range(len(bit_mask)):
        if not bit_mask[i] == "0":
            output += bit_mask[i]
        else:
            output += value[i]
    return output


def possible_addresses(bit_masked_address):
    output = []
    for bit_address in bit_masked_address:
        if "X" not in bit_address:
            return [bit_address]
        else:
            x_index = bit_address.index("X")
            for bit in ["0", "1"]:
                new_address = bit_address[:x_index] + bit + bit_address[x_index + 1:]
                val = possible_addresses([new_address])
                output += val
    return output


init_program = []
line = input()
while not line == "":
    init_program.append(line)
    line = input()

mask = ""
memory = {}
for ins in init_program:
    if ins[:4] == "mask":
        mask = ins.split(" = ")[1]
    else:
        address = ins.split("[")[1].split("]")[0]
        num = ins.split(" = ")[1]
        memory[address] = int(run_mask_part_1(bin(int(num))[2:].zfill(36), mask), 2)

total = 0
for (key, mem_value) in memory.items():
    total += mem_value
part_1_ans = total
print(part_1_ans)

mask = ""
memory = {}
for ins in init_program:
    if ins[:4] == "mask":
        mask = ins.split(" = ")[1]
    else:
        address = ins.split("[")[1].split("]")[0]
        num = ins.split(" = ")[1]
        masked_adr = run_mask_part_2(bin(int(address))[2:].zfill(36), mask)
        for pos_adr in possible_addresses([masked_adr]):
            memory[int(pos_adr, 2)] = num

total = 0
for (key, mem_value) in memory.items():
    total += int(mem_value)
part_2_ans = total
print(part_2_ans)
