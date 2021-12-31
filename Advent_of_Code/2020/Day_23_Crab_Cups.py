class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.index_dict = {}

    def append(self, value, in_node=None):
        node = in_node if in_node else Node(value)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def find_index_dict(self):
        next_node = self.head
        while next_node.next is not None:
            self.index_dict[next_node.value] = next_node
            next_node = next_node.next
        self.index_dict[next_node.value] = next_node
        return self.index_dict

    def find_node_by_value(self, value):
        return self.index_dict[value]

    @staticmethod
    def from_array(arr):
        output = LinkedList()
        output.append(arr[0])
        for elem in arr[1:]:
            output.append(elem)
        return output


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def simulate_moves(cups_input, n):
    cups_in = LinkedList.from_array(cups_input)

    # this creates a lookup dict mapping the cup labels to the cup nodes
    # this table will update itself so no manual updating is needed
    # this is because in the loop, the same nodes are just being attached and detached
    cups_index = cups_in.find_index_dict()

    # connect the end of the linked list to the head
    # this creates a circular linked list
    cups_in.tail.next = cups_in.head

    num_cups = len(cups_input)
    current_cup = cups_in.head
    for m in range(n):
        picked_up_cups_labels = set()
        next_cup = current_cup
        for _ in range(3):
            picked_up_cups_labels.add(next_cup.next.value)
            next_cup = next_cup.next
        picked_up_cups = LinkedList()
        picked_up_cups.append(0, in_node=cups_index[current_cup.next.value])

        destination = current_cup.value - 1
        if destination < 1:
            destination = num_cups
        while destination in picked_up_cups_labels:
            destination -= 1
            if destination < 1:
                destination = num_cups
        destination_node = cups_index[destination]
        destination_node_next = destination_node.next

        # attach the node after the last picked up cup to the node before the first picked up cup
        # this is to remove the cups that have been picked up
        current_cup.next = next_cup.next

        # insert the picked up cups linked list after the destination
        # this is done by first finding the last node in the picked up cups list
        # this list should only be three elements long, however it is circular
        # this is because no new nodes can be created for the lookup table to still be usable
        # the nodes after the destination are then attached to the end node
        # this linked list is then attached to the destination, completing the insertion
        end_node = picked_up_cups.head
        for _ in range(2):
            end_node = end_node.next
        end_node.next = destination_node_next
        destination_node.next = picked_up_cups.head

        current_cup = current_cup.next
    return cups_in


cups = [int(num) for num in input()]
cups_2 = cups.copy()
for i in range(len(cups_2) + 1, 1000001):
    cups_2.append(i)

cups = simulate_moves(cups, 100)
current_node = cups.find_node_by_value(1)
cup_string = ""
for i in range(9):
    cup_string += str(current_node.value)
    current_node = current_node.next
part_1_ans = cup_string[1:]
print(part_1_ans)

cups_2 = simulate_moves(cups_2, 10000000)
current_node = cups_2.find_node_by_value(1)
first_star = current_node.next
second_star = first_star.next
part_2_ans = first_star.value * second_star.value
print(part_2_ans)
