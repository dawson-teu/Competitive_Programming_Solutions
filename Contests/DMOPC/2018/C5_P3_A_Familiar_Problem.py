line = input()
n, m = [int(line.split(" ")[i]) for i in range(2)]
line = input()
cute_arr = line.split(" ")

left = 0
right = 0
count = 0
max_len = -1
while right < n:
    if count + int(cute_arr[right]) < m:
        if right - left + 1 > max_len:
            max_len = right - left + 1
        count += int(cute_arr[right])
        right += 1
    else:
        count -= int(cute_arr[left])
        left += 1
print(max_len)
