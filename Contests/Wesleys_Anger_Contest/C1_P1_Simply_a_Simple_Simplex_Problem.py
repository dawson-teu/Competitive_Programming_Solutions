def search(val):
    left = 0
    right = (10 ** 11)
    result = 0
    while left <= right:
        middle = (left + right) // 2
        middle_val = (middle * (middle - 1)) // 2
        if middle_val >= val:
            result = middle
            right = middle - 1
        else:
            left = middle + 1
    return result


t = int(input())
output = []
for i in range(t):
    output.append(search(int(input())))

for elem in output:
    print(elem)
