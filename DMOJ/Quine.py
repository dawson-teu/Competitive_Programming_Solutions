from string import punctuation

program = [
    "from string import punctuation",
    "program = [",
    "    ",
    "]",
    "for i in range(0, 2):",
    "    print(program[i])",
    "for line in program:",
    "    print(program[2] + punctuation[1] + line + punctuation[1] + ',')",
    "for i in range(3, len(program)):",
    "    print(program[i])",
]
for i in range(0, 2):
    print(program[i])
for line in program:
    print(program[2] + punctuation[1] + line + punctuation[1] + ',')
for i in range(3, len(program)):
    print(program[i])
