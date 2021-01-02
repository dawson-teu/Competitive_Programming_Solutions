t1 = int(input())
t2 = int(input())

seq = [t1, t2]
while seq[-1] <= seq[-2]:
    seq.append(seq[-2] - seq[-1])
print(len(seq))
