n = int(input())
output = []
for i in range(n):
    sequence = []
    input_seq = input().split(" ")
    for j in range(10):
        sequence.append(int(input_seq[j]))

    arith = True
    geo = True
    for j in range(2, len(sequence)):
        if not sequence[j] + sequence[j - 2] == 2 * sequence[j - 1]:
            arith = False
        if not sequence[j] * sequence[j - 2] == (sequence[j - 1] ** 2):
            geo = False
    if arith and geo:
        output.append("both")
    elif arith:
        output.append("arithmetic")
    elif geo:
        output.append("geometric")
    else:
        output.append("neither")

for elem in output:
    print(elem)
