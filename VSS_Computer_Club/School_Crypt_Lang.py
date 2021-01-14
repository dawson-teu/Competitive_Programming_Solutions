def encrypt(plaintext):
    ciphertext = ""
    for i in range(len(plaintext)):
        ascii_val = ord(plaintext[i])
        if (i + 1) % 2 == 0:
            change_value = (i + 1)
        else:
            change_value = -(i + 1)
        new_value = (ascii_val + change_value - 32) % 95 + 32
        ciphertext += chr(new_value)
    return ciphertext


def decrypt(ciphertext):
    plaintext = ""
    for i in range(len(ciphertext)):
        ascii_val = ord(ciphertext[i])
        if (i + 1) % 2 == 0:
            change_value = -(i + 1)
        else:
            change_value = (i + 1)
        new_value = (ascii_val + change_value - 32) % 95 + 32
        plaintext += chr(new_value)
    return plaintext


# print(decrypt("H\"eeokxUfxYml\"q"))
# print(decrypt("SFPFz\\bzk VxraVs^!Qu]0hkJ#T,O>$0L3R9@9XkC@7"))

command = input()
text = input()
if command == "encrypt":
    print(encrypt(text))
elif command == "decipher":
    print(decrypt(text))
