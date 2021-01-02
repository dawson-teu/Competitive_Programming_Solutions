t = int(input())
output = []
for _ in range(t):
    n = int(input())
    x = input().split(" ")
    x = [int(x[i]) for i in range(len(x))]
    y = input().split(" ")
    y = [int(y[i]) for i in range(len(y))]

    max_dist = 0
    for i in range(n):
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if y[mid] >= x[i]:
                left = mid + 1
            else:
                right = mid - 1
        max_dist = max(max_dist, (left + right) // 2 - i)
    output.append(max_dist)

for elem in output:
    print("The maximum distance is " + str(elem))
