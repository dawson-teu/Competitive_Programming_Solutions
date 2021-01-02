def row_num(string):
    string = string.replace("F", "0")
    string = string.replace("B", "1")
    return int(string, 2)


def col_num(string):
    string = string.replace("L", "0")
    string = string.replace("R", "1")
    return int(string, 2)


part_1_max = -1
part_2_arr = [False for i in range(1024)]
line = input()
while not line == "":
    row = line[:7]
    column = line[7:]
    seat_num = row_num(row) * 8 + col_num(column)
    part_1_max = max(part_1_max, seat_num)
    part_2_arr[seat_num] = True
    line = input()

part_2_ans = -1
for i in range(1, len(part_2_arr) - 1):
    if part_2_arr[i - 1] and part_2_arr[i + 1] and not part_2_arr[i]:
        part_2_ans = i

print(part_1_max)
print(part_2_ans)
