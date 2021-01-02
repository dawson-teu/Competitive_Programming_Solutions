k = int(input())
encoding = {}
for i in range(k):
    line = input()
    encoding[line.split(" ")[0]] = line.split(" ")[1]
string = input()

output = ""
while len(string) > 0:
    for (key, value) in encoding.items():
        if string.startswith(value):
            output += key
            string = string[len(value):]
            break
print(output)
