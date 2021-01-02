line_a = input()
line_b = input()

a_freq = {}
for i in range(len(line_a)):
    if not line_a[i] == " ":
        if line_a[i] in a_freq:
            a_freq[line_a[i]] += 1
        else:
            a_freq[line_a[i]] = 1

b_freq = {}
for i in range(len(line_b)):
    if not line_b[i] == " ":
        if line_b[i] in b_freq:
            b_freq[line_b[i]] += 1
        else:
            b_freq[line_b[i]] = 1

if not len(a_freq.items()) == len(b_freq.items()):
    print("Is not an anagram.")
else:
    anagram = True
    for (key, value) in a_freq.items():
        if not b_freq[key] == value:
            anagram = False
            break
    print("Is an anagram." if anagram else "Is not an anagram.")
