n = int(input())
s = input()

new_string = ""
x_count = 0
for i in range(len(s)):
    if s[i] == "X" and s[i + 1] == "X":
        x_count += 1
    elif s[i] == "X" and not s[i + 1] == "X":
        x_count += 1
        new_index = len(new_string) - x_count
        new_string = new_string[:new_index] + s[i + 1] + new_string[new_index + 1:]
        x_count = 0
    elif not s[i] == "X" and not s[i - 1] == "X":
        new_string += s[i]

output = []
for i in range(n):
    name = input()
    if new_string[i] == "A":
        output.append(
            f"Dear {name}, beloved artist, I would love to have you at my party. Come to my crib on April 20th.")
    elif new_string[i] == "O":
        output.append(f"Dear {name}, beloved occasion enthusiast, come to my crib to celebrate this very special day.")
    elif new_string[i] == "R":
        output.append(f"Dear {name}, April 20th is happening again this year. Don't miss out.")

for elem in output:
    print(elem)
