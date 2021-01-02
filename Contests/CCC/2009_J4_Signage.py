w = int(input())
words = "WELCOME TO CCC GOOD LUCK TODAY".split(" ")

message = []
line = words[0]
for i in range(1, len(words)):
    if len(line) + len(words[i]) + 1 <= w:
        line += "." + words[i]
    else:
        message.append(line)
        line = words[i]
message.append(line)

for i in range(len(message)):
    index = 0
    if message[i].count(".") > 0:
        while len(message[i]) < w:
            while not message[i][index] == ".":
                index += 1
                index %= len(message[i])
            message[i] = message[i][:index] + "." + message[i][index:]
            while message[i][index] == ".":
                index += 1
                index %= len(message[i])
    else:
        message[i] = message[i] + "." * (w - len(message[i]))

for line in message:
    print(line)
