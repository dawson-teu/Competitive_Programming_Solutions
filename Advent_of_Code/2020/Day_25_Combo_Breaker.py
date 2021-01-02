def find_loop_size(pub_key):
    loop_size = 0
    trans_value = 1
    while not trans_value == pub_key:
        trans_value *= 7
        trans_value %= 20201227
        loop_size += 1
    return loop_size


def transform_key(pub_key, n):
    trans_value = 1
    for _ in range(n):
        trans_value *= pub_key
        trans_value %= 20201227
    return trans_value


card_pub_key = int(input())
door_pub_key = int(input())

card_loop_size = find_loop_size(card_pub_key)
door_loop_size = find_loop_size(door_pub_key)

encryption_key = transform_key(card_pub_key, door_loop_size)
part_1_ans = encryption_key
print(part_1_ans)
