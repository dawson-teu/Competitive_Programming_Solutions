import math


def median(data):
    if len(data) % 2 == 0:
        result = data[(len(data) // 2) - 1] + data[(len(data) // 2)]
        if result % 2 == 0:
            return result // 2
        else:
            return result / 2
    else:
        return data[math.ceil(len(data) / 2) - 1]


n = int(input())
input_data = [int(n) for n in input().split(" ") if not n == '']
input_data.sort()
data_min = str(min(input_data))
data_max = str(max(input_data))
data_q1 = str(median(input_data[:math.floor(n / 2)]))
data_q2 = str(median(input_data))
data_q3 = str(median(input_data[(n - math.floor(n / 2)):]))
print(data_min + " " + data_max + " " + data_q1 + " " + data_q2 + " " + data_q3)
