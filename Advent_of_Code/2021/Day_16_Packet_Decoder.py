import math


def parse_bits_to_tree(bits_packet):
    version = int(bits_packet[:3], 2)
    bits_packet = bits_packet[3:]

    type_id = int(bits_packet[:3], 2)
    bits_packet = bits_packet[3:]

    data = []
    if type_id == 4:
        last_packet = False
        literal = ''
        while not last_packet:
            if bits_packet[0] == '0':
                last_packet = True
            literal += bits_packet[1:5]
            bits_packet = bits_packet[5:]
        data.append(int(literal, 2))
    else:
        length_type = bits_packet[:1]
        bits_packet = bits_packet[1:]

        if length_type == '0':
            sub_packets_bit_len = int(bits_packet[:15], 2)
            bits_packet = bits_packet[15:]

            while sub_packets_bit_len > 0:
                sub_packet, new_bits_packets = parse_bits_to_tree(bits_packet)
                # we keep of the number of bits we have left to read in sub_packets_bit_len
                # after we parse a sub packet, the difference between our original bit string and our new bit string
                # is the length of that sub packet, and we subtract that from the number of bits left to read
                sub_packets_bit_len -= len(bits_packet) - len(new_bits_packets)
                bits_packet = new_bits_packets
                data.append(sub_packet)
        elif length_type == '1':
            num_sub_packets = int(bits_packet[:11], 2)
            bits_packet = bits_packet[11:]

            for i in range(num_sub_packets):
                sub_packet, bits_packet = parse_bits_to_tree(bits_packet)
                data.append(sub_packet)

    return {'version': version, 'type': type_id, 'data': data}, bits_packet


def total_version_num_sum(packet_tree):
    if packet_tree['type'] == 4:
        return packet_tree['version']

    total_version = packet_tree['version']
    for sub_packet in packet_tree['data']:
        total_version += total_version_num_sum(sub_packet)
    return total_version


def parse_tree_to_expr_val(packet_tree):
    if packet_tree['type'] == 4:
        return packet_tree['data'][0]

    sub_packets = []
    for sub_packet in packet_tree['data']:
        sub_packets.append(parse_tree_to_expr_val(sub_packet))

    if packet_tree['type'] == 0:
        return sum(sub_packets)
    if packet_tree['type'] == 1:
        return math.prod(sub_packets)
    if packet_tree['type'] == 2:
        return min(sub_packets)
    if packet_tree['type'] == 3:
        return max(sub_packets)
    if packet_tree['type'] == 5:
        return 1 if sub_packets[0] > sub_packets[1] else 0
    if packet_tree['type'] == 6:
        return 1 if sub_packets[0] < sub_packets[1] else 0
    if packet_tree['type'] == 7:
        return 1 if sub_packets[0] == sub_packets[1] else 0


with open("InputFiles/Day_16.txt") as f:
    bits_transmission_hex = f.readline().rstrip()

bits_transmission = ''
for hex_char in bits_transmission_hex:
    bits_transmission += bin(int(hex_char, 16))[2:].zfill(4)

packets, _ = parse_bits_to_tree(bits_transmission)

part_1_ans = total_version_num_sum(packets)
print(part_1_ans)

part_2_ans = parse_tree_to_expr_val(packets)
print(part_2_ans)
