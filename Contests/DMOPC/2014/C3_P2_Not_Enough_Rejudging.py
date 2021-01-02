import math

n = int(input())

output = []
ir = 0
wa = 0
for i in range(n):
    sub = input()
    if sub == "AC":
        output.append("AC")
    elif sub == "WA":
        wa += 1
        output.append("0")
    elif sub == "TLE":
        output.append("WA")
    elif sub == "IR":
        ir += 1
        if ir <= 10:
            output.append("AC")
        elif ir <= 20:
            output.append("WA")
        else:
            output.append("IR")

wa_change = math.floor(wa * 0.3)
wa = 0
for i in range(len(output)):
    if output[i] == "0":
        wa += 1
        if wa <= wa_change:
            output[i] = "AC"
        else:
            output[i] = "WA"

for elem in output:
    print(elem)
