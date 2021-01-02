from string import ascii_lowercase as alpha

s = input()
print(sum([alpha.index(c) + 1 for c in s]))
