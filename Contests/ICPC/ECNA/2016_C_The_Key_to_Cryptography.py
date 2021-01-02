from string import ascii_uppercase as alpha

cipher_text = input()
secret_word = input()

key = secret_word
message = ""
for i in range(len(cipher_text)):
    decrypted_letter = alpha[(alpha.index(cipher_text[i]) - alpha.index(key[i])) % 26]
    message += decrypted_letter
    key += decrypted_letter
print(message)
