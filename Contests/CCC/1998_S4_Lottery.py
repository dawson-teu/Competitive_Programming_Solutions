def leftBracket(string, i):
    leftIndex = i - 2
    if string[leftIndex] == ")":
        count = 1
        leftIndex -= 1
        while not count == 0:
            if string[leftIndex] == ")":
                count += 1
            elif string[leftIndex] == "(":
                count -= 1
            leftIndex -= 1
    else:
        while leftIndex >= 0 and not string[leftIndex] == " ":
            leftIndex -= 1
    if leftIndex == -1:
        return "(" + string
    else:
        return string[:leftIndex + 1] + "(" + string[leftIndex + 1:]


def rightBracket(string, i):
    rightIndex = i + 2
    if string[rightIndex] == "(":
        count = 1
        rightIndex += 1
        while not count == 0:
            if string[rightIndex] == "(":
                count += 1
            elif string[rightIndex] == ")":
                count -= 1
            rightIndex += 1
    else:
        while rightIndex < len(string) and not string[rightIndex] == " ":
            rightIndex += 1
    if rightIndex == len(string):
        return string + ")"
    else:
        return string[:rightIndex] + ")" + string[rightIndex:]


n = int(input())
lines = [input() for i in range(n)]
for line in lines:
    index = 0
    while index < len(line):
        while index < len(line) and not line[index] == "X":
            index += 1
        if index < len(line):
            line = leftBracket(line, index)
            line = rightBracket(line, index + 1)
        index += 2

    index = 0
    while index < len(line):
        while index < len(line) and not line[index] == "+" and not line[index] == "-":
            index += 1
        if index < len(line):
            line = leftBracket(line, index)
            line = rightBracket(line, index + 1)
        index += 2
    print(line[1:len(line) - 1])
