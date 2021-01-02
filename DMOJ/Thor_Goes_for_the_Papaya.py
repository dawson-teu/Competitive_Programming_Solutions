from string import ascii_uppercase as alpha

n = int(input())
code = [int(input()) for i in range(n)]

output = "Thanos is on Planet: "
for i in range(n - 1):
    output += alpha[code[i] * code[i + 1] % 26]
print(output)
