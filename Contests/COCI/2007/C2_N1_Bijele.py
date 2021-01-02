correct_num = [1, 1, 2, 2, 2, 8]
pieces = input().split(" ")

output = []
for i in range(len(correct_num)):
    output.append(str(correct_num[i] - int(pieces[i])))

print(" ".join(output))
