line = input()
n, m = [int(line.split(" ")[i]) for i in range(2)]

min_orp = [-1, -1]
for i in range(n):
    line = input().split(" ")
    num_good_cute = 0
    for j in range(m):
        cute = int(line[j])
        if 2 <= cute <= 9:
            num_good_cute += 1
    if num_good_cute > min_orp[0]:
        min_orp = [num_good_cute, i + 1]
print(min_orp[1])
