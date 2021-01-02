from string import ascii_lowercase as alpha

n = int(input())
output = []
for i in range(n):
    line = input().lower()
    ans = ""
    index = 0
    for j in range(len(line)):
        if line[j] in alpha:
            ans += (line[j].upper() if index % 2 == 1 else line[j])
            index += 1
        else:
            ans += line[j]
    output.append(ans)

for elem in output:
    print(elem)
