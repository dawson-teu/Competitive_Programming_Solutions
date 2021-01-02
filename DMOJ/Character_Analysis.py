def freq(string):
    d = {}
    for char in string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d


a = input()
b = input()

a_freq = freq(a)
b_freq = freq(b)
for (key, val) in a_freq.items():
    if key in b_freq:
        if not b_freq[key] == a_freq[key]:
            print(key)
            break
    else:
        print(key)
        break
