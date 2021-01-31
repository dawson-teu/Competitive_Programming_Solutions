def possible_moves(coin_pos):
    moves = []
    for i in range(len(coin_pos)):
        if not coin_pos[i] == "":
            if i > 0 and (coin_pos[i - 1] == "" or int(coin_pos[i - 1][0]) > int(coin_pos[i][0])):
                new_coin_pos = list(coin_pos)
                new_coin_pos[i - 1] = coin_pos[i][0] + coin_pos[i - 1]
                new_coin_pos[i] = coin_pos[i][1:]
                moves.append(tuple(new_coin_pos))
            if i < len(coin_pos) - 1 and (coin_pos[i + 1] == "" or int(coin_pos[i + 1][0]) > int(coin_pos[i][0])):
                new_coin_pos = list(coin_pos)
                new_coin_pos[i + 1] = coin_pos[i][0] + coin_pos[i + 1]
                new_coin_pos[i] = coin_pos[i][1:]
                moves.append(tuple(new_coin_pos))
    return moves


n = int(input())
while not n == 0:
    cur_coins = tuple(input().split(" "))

    goal_coins = tuple([str(i + 1) for i in range(len(cur_coins))])
    visited = {cur_coins: True}
    queue = [cur_coins]
    dist = {cur_coins: 0}
    min_dist = -1
    while len(queue) > 0:
        coins = queue.pop(0)
        if coins == goal_coins:
            min_dist = dist[coins]
            break
        for neighbour in possible_moves(coins):
            if neighbour not in visited or not visited[neighbour]:
                visited[neighbour] = True
                dist[neighbour] = dist[coins] + 1
                queue.append(neighbour)
    if min_dist == -1:
        print("IMPOSSIBLE")
    else:
        print(min_dist)
    n = int(input())
