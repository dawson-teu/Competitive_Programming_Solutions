def is_a(string):
    if string == "A":
        return True
    elif len(string) >= 3 and string[0] == "B" and string[-1] == "S" and is_monkey(string[1:-1]):
        return True
    else:
        return False


def is_monkey(string):
    if is_a(string):
        return True
    else:
        found = False
        for i in range(1, len(string) - 1):
            if is_a(string[:i]) and string[i] == "N" and is_monkey(string[i + 1:]):
                found = True
                break
        return found


line = input()
output = []
while not line == "X":
    output.append("YES" if is_monkey(line) else "NO")
    line = input()

for elem in output:
    print(elem)
