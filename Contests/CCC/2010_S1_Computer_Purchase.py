n = int(input())
arr = []
for i in range(n):
    line = input()
    name, r, s, d = line.split(" ")
    arr.append([name, 2 * int(r) + 3 * int(s) + int(d)])
arr = sorted(arr, key=lambda x: x[0])
arr = sorted(arr, key=lambda x: x[1], reverse=True)
if len(arr) > 1:
    print(arr[0][0])
    print(arr[1][0])
elif len(arr) == 1:
    print(arr[0][0])
