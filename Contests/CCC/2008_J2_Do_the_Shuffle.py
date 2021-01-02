playlist = ["A", "B", "C", "D", "E"]
b = int(input())
n = int(input())
while not (b == 4 and n == 1):
    if b == 1:
        for i in range(n):
            playlist = playlist[1:] + [playlist[0]]
    elif b == 2:
        for i in range(n):
            playlist = [playlist[-1]] + playlist[:4]
    elif b == 3:
        for i in range(n):
            playlist = [playlist[1]] + [playlist[0]] + playlist[2:]
    b = int(input())
    n = int(input())
print(" ".join(playlist))
