from string import ascii_lowercase as alpha

s = input()
q = int(input())

prefix_arr = []
for letter in alpha:
    prefix_arr.append([0])

for i in range(len(s)):
    for char in alpha:
        if s[i] == char:
            prefix_arr[alpha.index(char)].append(prefix_arr[alpha.index(char)][i] + 1)
        else:
            prefix_arr[alpha.index(char)].append(prefix_arr[alpha.index(char)][i])

output = []
for i in range(q):
    line = input()
    a, b, c = line.split(" ")
    output.append(
        prefix_arr[alpha.index(c)][int(b)] - (0 if int(a) - 1 < 0 else prefix_arr[alpha.index(c)][int(a) - 1]))

for elem in output:
    print(elem)
