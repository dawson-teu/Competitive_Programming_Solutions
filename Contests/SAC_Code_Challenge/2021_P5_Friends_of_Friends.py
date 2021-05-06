def find(elem, disjoint_set):
    if not elem == disjoint_set[elem - 1]:
        disjoint_set[elem - 1] = find(disjoint_set[elem - 1], disjoint_set)
    return disjoint_set[elem - 1]


n, q = map(int, input().split())
disjoint = [i + 1 for i in range(n)]
size_sets = [1 for i in range(n)]
for _ in range(q):
    query = input().split()
    if query[0] == "1":
        root1 = find(int(query[1]), disjoint)
        root2 = find(int(query[2]), disjoint)
        if not root1 == root2:
            disjoint[root1 - 1] = root2
            size_sets[root2 - 1] = size_sets[root1 - 1] + size_sets[root2 - 1]
    else:
        print(size_sets[find(int(query[1]), disjoint) - 1])
