string = input()
k = int(input())

substrings = []
for i in range(0, len(string) - k + 1):
    substrings.append(string[i:i + k])

print(sorted(substrings)[0])
