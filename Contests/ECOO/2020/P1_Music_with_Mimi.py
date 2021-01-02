scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C']


def is_v7(notes):
    pos = [scale.index(note) for note in notes]
    dif = [(pos[k + 1] - pos[k]) % 12 for k in range(3)]
    return dif[0] == 4 and dif[1] == 3 and dif[2] == 3


t = int(input())
output = []
for _ in range(t):
    chord = input().split()
    ans = -1
    for i in range(4):
        if is_v7(chord[i:] + chord[:i]):
            ans = (4 - i) % 4
    if ans == 0:
        output.append("root")
    elif ans == 1:
        output.append("first")
    elif ans == 2:
        output.append("second")
    elif ans == 3:
        output.append("third")
    elif ans == -1:
        output.append("invalid")

for elem in output:
    print(elem)
