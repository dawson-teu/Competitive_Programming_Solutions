import math


def ext_euc_alg(a, b):
    prev_r, r = a, b
    prev_s, s = 1, 0
    prev_t, t = 0, 1

    while not r == 0:
        q = prev_r // r
        prev_r, r = r, prev_r - q * r
        prev_s, s = s, prev_s - q * s
        prev_t, t = t, prev_t - q * t

    return prev_s, prev_t


depart_time = int(input())
bus_times = [bus_id for bus_id in input().split(",")]

# part 1
wait_time = math.inf
wait_id = -1
for bus_time in bus_times:
    if bus_time == "x":
        continue
    bus_time = int(bus_time)
    new_wait_time = bus_time * math.ceil(depart_time / bus_time) - depart_time
    if new_wait_time <= wait_time:
        wait_time = new_wait_time
        wait_id = bus_time
part_1_ans = wait_time * wait_id
print(part_1_ans)

# part 2
congruences = []
for i in range(len(bus_times)):
    if not bus_times[i] == "x":
        congruences.append((int(bus_times[i]) - i, int(bus_times[i])))

x, y = ext_euc_alg(congruences[0][1], congruences[1][1])
new_sol = congruences[0][0] * y * congruences[1][1]
new_sol += congruences[1][0] * x * congruences[0][1]
new_n = congruences[0][1] * congruences[1][1]
for i in range(2, len(congruences)):
    x, y = ext_euc_alg(new_n, congruences[i][1])
    new_sol = new_sol * y * congruences[i][1]
    new_sol += congruences[i][0] * x * new_n
    new_n *= congruences[i][1]

part_2_ans = new_sol - (new_sol // new_n) * new_n
print(part_2_ans)
