import sys


def cost_to_remove(node):
    total = costs[node]
    for child in children[node]:
        total += cost_to_remove(child)
    remove_cost[node] = total
    return total


def min_cost(node):
    if len(children[node]) == 0:
        return costs[node]
    else:
        max_children = 2
        if node == 0:
            max_children = 3
        sub_trees = []
        for child in children[node]:
            sub_trees.append((min_cost(child), child))
        keep = []
        for _ in range(min(max_children, len(children[node]))):
            max_child = (-1, 0)
            for cost in sub_trees:
                if cost[0] <= max_child[0]:
                    continue
                cond = len(keep) != 0 and (keep[-1][0] > cost[0] or (keep[-1][0] == cost[0] and keep[-1][1] != cost[1]))
                if len(keep) == 0 or cond:
                    max_child = cost
            keep.append(max_child)
        total = remove_cost[node] - costs[node]
        for cost in keep:
            total -= cost[0]
        return remove_cost[node] - total


n = int(sys.stdin.readline())
costs = [0] + list(map(int, sys.stdin.readline().split()))
adj_list: list[list[int]] = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a - 1].append(b - 1)
    adj_list[b - 1].append(a - 1)
children: list[list[int]] = [[] for _ in range(n)]
stack = [0]
visited = [False for _ in range(n)]
visited[0] = True
while len(stack) > 0:
    vertex = stack.pop()
    for neighbour in adj_list[vertex]:
        if not visited[neighbour]:
            children[vertex].append(neighbour)
            stack.append(neighbour)
            visited[neighbour] = True

remove_cost = [0 for _ in range(n)]
cost_to_remove(0)

print(remove_cost[0] - min_cost(0))
