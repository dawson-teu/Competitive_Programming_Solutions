from string import ascii_uppercase as alpha

k = int(input())
s = input()

print("".join([alpha[(alpha.index(s[i]) - (3 * (i + 1) + k)) % 26] for i in range(len(s))]))
