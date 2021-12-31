# the dp (memo) state is the current node, history (visited) and whether the single lower node has already been used
def dfs(node, in_adj_list, visited, used_single, memo):
    if (node, tuple(visited), used_single) in memo:
        return memo[(node, tuple(visited), used_single)]
    if node == 'end':
        return 1
    total_paths = 0
    for neighbour in in_adj_list[node]:
        # if the neighbour is an upper node, or it is an unvisited lower node, we can visit without restrictions
        # however if it is a visited lower node then we can only visit if we use our previously unused single lower node
        if neighbour.isupper() or (neighbour.islower() and neighbour not in visited):
            total_paths += dfs(neighbour, in_adj_list, visited.union({node}), used_single, memo)
        elif not used_single and neighbour.islower() and neighbour in visited and neighbour not in ['start', 'end']:
            total_paths += dfs(neighbour, in_adj_list, visited.union({node}), True, memo)
    memo[(node, tuple(visited), used_single)] = total_paths
    return total_paths


with open("InputFiles/Day_12.txt") as f:
    adj_list = {}
    for line in f:
        cave_a, cave_b = line.rstrip().split('-')
        if cave_a in adj_list:
            adj_list[cave_a].append(cave_b)
        else:
            adj_list[cave_a] = [cave_b]

        if cave_b in adj_list:
            adj_list[cave_b].append(cave_a)
        else:
            adj_list[cave_b] = [cave_a]

# for part 1 no lower nodes can be visited twice, so it is as if the single lower node has already been used
part_1_ans = dfs('start', adj_list, set(), True, {})
print(part_1_ans)

part_2_ans = dfs('start', adj_list, set(), False, {})
print(part_2_ans)
