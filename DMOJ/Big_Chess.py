w = int(input())
h = int(input())

h_val = False
output = []
for i in range(h):
    w_val = h_val
    line = ""
    for j in range(w):
        line += "1" if w_val else "0"
        w_val = not w_val
    output.append(line)
    h_val = not h_val

for elem in output:
    print(elem)
