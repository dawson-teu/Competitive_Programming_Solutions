import sys


def is_arithmetic_seq(string):
    d1 = int(string[1]) - int(string[0])
    d2 = int(string[2]) - int(string[1])
    if len(string) == 4:
        d3 = int(string[3]) - int(string[2])
        return d1 == d2 == d3
    return d1 == d2


def find_count(num):
    count = 0
    cur_time = "1200"
    for _ in range(num):
        if is_arithmetic_seq(cur_time):
            count += 1
        minutes = int(cur_time[-2:])
        hours = int(cur_time[:-2])
        if minutes + 1 >= 60:
            hours += 1
            minutes = 0
        else:
            minutes += 1
        if hours > 12:
            hours = 1
        cur_time = str(hours) + str(minutes).rjust(2, "0")
    return count


d = int(sys.stdin.readline())
if d > 720:
    print(find_count(720) * (d // 720) + find_count(d % 720 + 1))
else:
    print(find_count(d + 1))
