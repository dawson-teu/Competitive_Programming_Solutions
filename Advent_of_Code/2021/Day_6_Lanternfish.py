with open("InputFiles/Day_6.txt") as f:
    start_fishes = [int(num) for num in f.readline().split(',')]

fishes = start_fishes
for i in range(80):
    new_fish = []
    for fish in fishes:
        if fish == 0:
            new_fish.append(6)
            new_fish.append(8)
        else:
            new_fish.append(fish - 1)
    fishes = new_fish
part_1_ans = len(fishes)
print(part_1_ans)

fish_freq = {i: 0 for i in range(9)}
for fish in start_fishes:
    fish_freq[fish] += 1
for i in range(256):
    new_fish_freq = {i: 0 for i in range(9)}
    for timer, freq in fish_freq.items():
        if timer == 0:
            new_fish_freq[6] += freq
            new_fish_freq[8] += freq
        else:
            new_fish_freq[timer - 1] += freq
    fish_freq = new_fish_freq
part_2_ans = 0
for _, freq in fish_freq.items():
    part_2_ans += freq
print(part_2_ans)
