alpha = input()
string = input()

output = {string}
for i in range(len(string)):
    output.add(string[:i] + string[i + 1:])
    for letter in alpha:
        output.add(string[:i] + letter + string[i:])
        output.add(string[:i] + letter + string[i + 1:])
for letter in alpha:
    output.add(string + letter)
for elem in sorted(list(output)):
    if not elem == string:
        print(elem)
