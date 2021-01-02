c = int(input())
set_bool = []

output = []
for i in range(c):
    command = input().split(' ')
    if command[0] == '1':
        if command[1] in set_bool:
            output.append('false')
        else:
            output.append('true')
            set_bool.append(command[1])
    elif command[0] == '2':
        if command[1] in set_bool:
            output.append('true')
            set_bool.remove(command[1])
        else:
            output.append('false')
    elif command[0] == '3':
        if command[1] in set_bool:
            output.append(str(set_bool.index(command[1])))
        else:
            output.append('-1')
    elif command[0] == '4':
        sorted_set = []
        if 'false' in set_bool:
            sorted_set.append('false')
        if 'true' in set_bool:
            sorted_set.append('true')
        output.append(" ".join(sorted_set))

for elem in output:
    print(elem)
