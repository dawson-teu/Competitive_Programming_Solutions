bin_oct = {
    '000': '0',
    '001': '1',
    '010': '2',
    '011': '3',
    '100': '4',
    '101': '5',
    '110': '6',
    '111': '7'
}

num = input()
num = ((3 * (len(num) // 3 + 1) - len(num)) * '0' if not len(num) % 3 == 0 else '') + num

output = ""
for i in range(0, len(num), 3):
    output += bin_oct[num[i:i + 3]]
print(output)
