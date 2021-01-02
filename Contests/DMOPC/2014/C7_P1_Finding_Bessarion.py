n = int(input())

bessarion_pos = -1
stations = []
for i in range(n):
    stations.append(input())
    if stations[i] == "Bessarion":
        bessarion_pos = i
try:
    prev = stations[bessarion_pos - 1]
    nex = stations[bessarion_pos + 1]
    if prev == "Leslie" and nex == "Bayview" or prev == "Bayview" and nex == "Leslie":
        print("Y")
    else:
        print("N")
except IndexError:
    print("N")
