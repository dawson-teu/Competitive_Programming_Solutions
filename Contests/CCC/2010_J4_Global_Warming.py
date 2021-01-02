output = []
seq = input().strip(" ").split(" ")

while not int(seq[0]) == 0:
    n = int(seq[0])
    seq = seq[1:]

    diff = []
    for i in range(1, len(seq)):
        diff.append(int(seq[i]) - int(seq[i - 1]))

    stack = []
    for i in range(len(diff)):
        if len(stack) == 0:
            stack = diff[:i + 1]
        elif not stack[i % len(stack)] == diff[i]:
            stack = diff[:i + 1]
    output.append(len(stack))
    seq = input().strip(" ").split(" ")

for elem in output:
    print(elem)
