n = int(input())

arr = [i + 1 for i in range(n)]
for i in range(n - 1):
    num = int(input())
    arr.remove(num)
print(arr[0])
