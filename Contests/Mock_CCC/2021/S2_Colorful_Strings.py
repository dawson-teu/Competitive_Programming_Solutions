from string import ascii_lowercase as alpha

string = input()
freq = {alpha_letter: 0 for alpha_letter in alpha}
for letter in string:
    freq[letter] += 1
count = 1
for (letter, value) in freq.items():
    count *= (value + 1)
print(count % (10 ** 9 + 7))
