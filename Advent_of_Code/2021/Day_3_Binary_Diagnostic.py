with open("InputFiles/Day_3.txt") as f:
    report = []
    for line in f:
        report.append(line.rstrip())

# part 1
epsilon = ''
gamma = ''
for i in range(len(report[0])):
    count_0 = 0
    count_1 = 1
    for j in range(len(report)):
        if report[j][i] == '0':
            count_0 += 1
        else:
            count_1 += 1
    if count_1 > count_0:
        epsilon += '0'
        gamma += '1'
    elif count_0 > count_1:
        epsilon += '1'
        gamma += '0'
part_1_ans = int(epsilon, 2) * int(gamma, 2)
print(part_1_ans)

# part 2
oxy_rating = report
for i in range(len(report[0])):
    if len(oxy_rating) == 1:
        break

    count_0 = 0
    count_1 = 0
    for j in range(len(oxy_rating)):
        if oxy_rating[j][i] == '0':
            count_0 += 1
        else:
            count_1 += 1

    new_oxy_rating = []
    for number in oxy_rating:
        if (count_0 > count_1 and number[i] == '0') or (count_0 <= count_1 and number[i] == '1'):
            new_oxy_rating.append(number)
    oxy_rating = new_oxy_rating

co2_rating = report
for i in range(len(report[0])):
    if len(co2_rating) == 1:
        break

    count_0 = 0
    count_1 = 0
    for j in range(len(co2_rating)):
        if co2_rating[j][i] == '0':
            count_0 += 1
        else:
            count_1 += 1

    new_co2_rating = []
    for number in co2_rating:
        if (count_0 <= count_1 and number[i] == '0') or (count_0 > count_1 and number[i] == '1'):
            new_co2_rating.append(number)
    co2_rating = new_co2_rating
part_2_ans = int(oxy_rating[0], 2) * int(co2_rating[0], 2)
print(part_2_ans)
