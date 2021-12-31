import heapq


def part_1_edge_weight(new_pos):
    return grid[new_pos[1]][new_pos[0]]


def part_2_edge_weight(new_pos):
    # for part 2, we only store the original grid, since the full grid is formed from sub-grids based on the original
    # for any position in the full grid, the risk level can be found by first finding its position in its sub-grid
    # since sub-grids are repeated versions of the original, this can be easily done with modulus
    # next we add the Manhattan distance between the sub-grid and the original (each repetition adds one to the risk)
    # finally if the risk level is above 9, we wrap back to 1 using modulus
    return ((grid[new_pos[1] % size][new_pos[0] % size] + new_pos[1] // size + new_pos[0] // size - 1) % 9) + 1


def dijkstra(start: tuple[int, int], end, calc_edge_weight, grid_size):
    dist = [[10 ** 10 for _ in range(grid_size)] for _ in range(grid_size)]
    dist[start[1]][start[0]] = 0

    visited = [[False for _ in range(grid_size)] for _ in range(grid_size)]
    visited[start[1]][start[0]] = True

    priority_queue = [(dist[start[1]][start[0]], start)]
    while len(priority_queue) > 0:
        _, cur_pos = heapq.heappop(priority_queue)
        if cur_pos == end:
            break

        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos: tuple[int, int] = (cur_pos[0] + move[0], cur_pos[1] + move[1])
            if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size and not visited[new_pos[1]][new_pos[0]]:
                # calc_edge_weight returns the risk added when moving between cur_pos and new_pos
                # this can also be thought of as the weight of the edge connecting them
                new_dist = dist[cur_pos[1]][cur_pos[0]] + calc_edge_weight(new_pos)
                if dist[new_pos[1]][new_pos[0]] > new_dist:
                    dist[new_pos[1]][new_pos[0]] = new_dist
                    visited[new_pos[1]][new_pos[0]] = True
                    heapq.heappush(priority_queue, (dist[new_pos[1]][new_pos[0]], new_pos))
    return dist[end[1]][end[0]]


with open("InputFiles/Day_15.txt") as f:
    grid = []
    for line in f:
        grid.append([int(num) for num in line.rstrip()])
    size = len(grid)

part_1_ans = dijkstra((0, 0), (size - 1, size - 1), part_1_edge_weight, size)
print(part_1_ans)

part_2_ans = dijkstra((0, 0), (size * 5 - 1, size * 5 - 1), part_2_edge_weight, size * 5)
print(part_2_ans)
