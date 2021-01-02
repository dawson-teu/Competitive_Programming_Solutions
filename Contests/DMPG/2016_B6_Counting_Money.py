def base2to10(s):
    total = 0
    for k in range(len(s)):
        total += int(s[k]) * ((-2) ** (len(s) - k - 1))
    return total


def base10to2(num):
    string = ""
    while not num == 0:
        mod = num % -2
        num = num // -2
        if mod < 0:
            mod += 2
            num += 1
        string = str(mod) + string
    if string == "":
        return "0"
    else:
        return string


n = int(input())
output = []
for i in range(n):
    x, y = input().split(" ")
    if x == "A":
        output.append(base2to10(y))
    else:
        output.append(base10to2(int(y)))

for elem in output:
    print(elem)
