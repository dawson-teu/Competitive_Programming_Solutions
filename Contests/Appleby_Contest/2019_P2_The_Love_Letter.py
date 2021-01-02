from string import ascii_lowercase as alpha

n = int(input())
k = int(input())
letter = input()

output = ""
for i in range(n):
    if letter[i] == " ":
        output += " "
    else:
        output += alpha[(alpha.index(letter[i]) + k) % 26]
print(output)
