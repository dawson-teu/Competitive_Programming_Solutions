from string import ascii_lowercase as alpha


def base26(num, pad=True):
    if not pad:
        return alpha[num]
    num_base26 = [num // (26 ** 1), (num % (26 ** 1)) // (26 ** 0)]
    return "".join([alpha[digit] for digit in num_base26])


def base10(string):
    total = 0
    for i in range(len(string)):
        total += 26 ** (len(string) - i - 1) * alpha.index(string[i])
    return total


def encrypt(string, key):
    header = base26(len(string.split(" ")))
    for word in string.split(" "):
        header += base26(len(word), pad=False)
    string = header + string

    encrypted = ""
    total = 0
    for i in range(len(string) - 1, -1, -1):
        if not string[i] == " ":
            encrypted = alpha[(alpha.index(string[i]) + key + total) % 26] + encrypted
            total += alpha.index(string[i])
    return encrypted


def decrypt(string, key):
    decrypted = ""
    total = 0
    for i in range(len(string) - 1, -1, -1):
        decrypted = alpha[(alpha.index(string[i]) - key - total) % 26] + decrypted
        total += alpha.index(decrypted[0])
    string = decrypted

    decrypted = ""
    num_words = base10(string[:2])
    length_words = [base10(string[i]) for i in range(2, 2 + num_words)]
    cur_word_index = 0
    cur_word_length = 0
    for i in range(2 + num_words, len(string)):
        decrypted += string[i]
        cur_word_length += 1
        if cur_word_length == length_words[cur_word_index]:
            cur_word_index += 1
            cur_word_length = 0
            decrypted += " "
    return decrypted


output = []
for _ in range(10):
    n = int(input())
    message = input()
    if " " in message:
        output.append(encrypt(message, n))
    else:
        output.append(decrypt(message, n))

for elem in output:
    print(elem)
