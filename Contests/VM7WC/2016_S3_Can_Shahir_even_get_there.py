def neighbours(vertex, graph_edges):
    neighbour_edges = []
    for edge in graph_edges:
        if edge[0] == vertex:
            neighbour_edges.append(edge[1])
        elif edge[1] == vertex:
            neighbour_edges.append(edge[0])
    return neighbour_edges


def dfs(source, target, graph_edges):
    stack = []
    visited = []
    stack.insert(0, source)
    while len(stack) > 0:
        vertex = stack.pop(0)
        if vertex == target:
            return True
        if vertex not in visited:
            visited.append(vertex)
            stack += neighbours(vertex, graph_edges)
    return False


n, m, a, b = [int(num) for num in input().split(" ")]
edges = [[int(vertex) for vertex in input().split(" ")] for i in range(m)]
print("GO SHAHIR!" if dfs(a, b, edges) else "NO SHAHIR!")
