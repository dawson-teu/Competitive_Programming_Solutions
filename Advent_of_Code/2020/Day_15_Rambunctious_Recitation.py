starting_nums = [int(num) for num in input().split(",")]

spoken_words = {}
last_num_spoken = None
for i in range(1, 2001):
    spoken = -1
    if i <= len(starting_nums):
        spoken = starting_nums[i - 1]
    elif len(spoken_words[last_num_spoken]) > 1:
        spoken = spoken_words[last_num_spoken][-1] - spoken_words[last_num_spoken][-2]
    else:
        spoken = 0
    if spoken in spoken_words:
        spoken_words[spoken].append(i)
    else:
        spoken_words[spoken] = [i]
    last_num_spoken = spoken
part_1_ans = last_num_spoken
print(part_1_ans)

for i in range(2001, 30000001):
    spoken = -1
    if i <= len(starting_nums):
        spoken = starting_nums[i - 1]
    elif len(spoken_words[last_num_spoken]) > 1:
        spoken = spoken_words[last_num_spoken][-1] - spoken_words[last_num_spoken][-2]
    else:
        spoken = 0
    if spoken in spoken_words:
        spoken_words[spoken].append(i)
    else:
        spoken_words[spoken] = [i]
    last_num_spoken = spoken
part_2_ans = last_num_spoken
print(part_2_ans)
