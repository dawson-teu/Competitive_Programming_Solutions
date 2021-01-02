def count_possible_permutations(n, memo):
    if n == ratings[-1]:
        return 1
    if n in memo:
        return memo[n]
    count = 0
    for j in range(1, 4):
        if n + j in ratings_set:
            count += count_possible_permutations(n + j, memo)
    memo[n] = count
    return count


ratings = []
line = input()
while not line == "":
    ratings.append(int(line))
    line = input()
ratings.append(0)
ratings = sorted(ratings)
ratings.append(ratings[-1] + 3)

num_diff_1 = 0
num_diff_3 = 0
for i in range(1, len(ratings)):
    diff = ratings[i] - ratings[i - 1]
    if diff == 1:
        num_diff_1 += 1
    elif diff == 3:
        num_diff_3 += 1
part_1_ans = num_diff_1 * num_diff_3
print(part_1_ans)

ratings_set = set(ratings)
memo_dict = {}
part_2_ans = count_possible_permutations(0, memo_dict)
print(part_2_ans)
