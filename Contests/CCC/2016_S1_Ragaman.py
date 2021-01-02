def freq(string):
    d = {}
    for char in string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d


line1 = input()
line2 = input()

if not len(line1) == len(line2):
    print("N")

line1_dict = freq(line1)
line2_dict = freq(line2)
anagram = True
for (key, value) in line1_dict.items():
    if line1_dict[key] < (line2_dict[key] if key in line2_dict else 0):
        anagram = False
    elif line1_dict[key] > (line2_dict[key] if key in line2_dict else 0) and "*" in line2_dict and line2_dict["*"] - (
            line1_dict[key] - (line2_dict[key] if key in line2_dict else 0)) >= 0:
        line2_dict["*"] -= line1_dict[key] - (line2_dict[key] if key in line2_dict else 0)
    elif line1_dict[key] > (line2_dict[key] if key in line2_dict else 0):
        anagram = False
print("A" if anagram else "N")
