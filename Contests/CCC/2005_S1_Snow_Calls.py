from string import ascii_uppercase as alpha

num_to_str = {
    "A": 2,
    "B": 2,
    "C": 2,
    "D": 3,
    "E": 3,
    "F": 3,
    "G": 4,
    "H": 4,
    "I": 4,
    "J": 5,
    "K": 5,
    "L": 5,
    "M": 6,
    "N": 6,
    "O": 6,
    "P": 7,
    "Q": 7,
    "R": 7,
    "S": 7,
    "T": 8,
    "U": 8,
    "V": 8,
    "W": 9,
    "X": 9,
    "Y": 9,
    "Z": 9,
}

n = int(input())
numbers = [input() for i in range(n)]

output = []
for i in range(n):
    answer = ""
    for char in numbers[i]:
        if char in "0123456789":
            answer += char
        elif char in alpha:
            answer += str(num_to_str[char])
    output.append(answer[:3] + "-" + answer[3:6] + "-" + answer[6:10])

for elem in output:
    print(elem)
