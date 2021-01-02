from string import ascii_uppercase as alpha


def shift(char, k):
    return alpha[(alpha.index(char) + alpha.index(k)) % 26]


key = input()
message = input()

new_message = ""
for letter in message:
    if letter in alpha:
        new_message += letter
message = new_message

output = ""
for i in range(len(message)):
    if message[i] in alpha:
        output += shift(message[i], key[i % len(key)])
print(output)
