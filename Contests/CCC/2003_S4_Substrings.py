def lcp(str_a, str_b):
    min_len = min(len(str_a), len(str_b))
    for j in range(min_len):
        if not str_a[j:j + 1] == str_b[j:j + 1]:
            return j
    return min_len


n = int(input())
output = []
for _ in range(n):
    string = input()
    suffix_arr = []
    for i in range(len(string)):
        suffix_arr.append(string[i:])
    suffix_arr = sorted(suffix_arr)

    count = len(suffix_arr[0])
    for i in range(1, len(string)):
        count += len(suffix_arr[i]) - lcp(suffix_arr[i], suffix_arr[i - 1])
    output.append(count + 1)

for elem in output:
    print(elem)
