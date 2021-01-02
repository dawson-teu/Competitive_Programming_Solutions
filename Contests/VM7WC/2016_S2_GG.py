g_string = input()

prefix_sum_arr = [(1 if g_string[0] == "G" else 0)]
for i in range(1, len(g_string)):
    prefix_sum_arr.append(prefix_sum_arr[i - 1] + (1 if g_string[i] == "G" else 0))

n = int(input())
output = []
for i in range(n):
    query = [int(num) for num in input().split(" ")]
    if query[0] > 0:
        output.append(prefix_sum_arr[query[1]] - prefix_sum_arr[query[0] - 1])
    else:
        output.append(prefix_sum_arr[query[1]])

for elem in output:
    print(elem)
