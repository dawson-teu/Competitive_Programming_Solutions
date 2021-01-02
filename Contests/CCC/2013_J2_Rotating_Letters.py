valid_letters = ['i', 'o', 's', 'h', 'z', 'x', 'n']
flag = True
word = input()
for letter in word:
    if not letter.lower() in valid_letters:
        print('NO')
        flag = False
        break
if flag:
    print('YES')
