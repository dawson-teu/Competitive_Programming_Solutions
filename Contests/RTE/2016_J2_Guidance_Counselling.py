import heapq

color_val = {
    "BLUE": 0,
    "PINK": 1,
    "GREEN": 2
}


def format_val(val):
    return list(color_val.keys())[val[0]] + " " + val[1]


q = int(input())

p_queue = []
output = []
for i in range(q):
    query = input()
    if query == "NEXT" and len(p_queue) == 0:
        output.append("NONE")
    elif query == "NEXT":
        output.append(format_val(heapq.heappop(p_queue)))
    else:
        c = query.split(" ")[1]
        m = query.split(" ")[2]
        heapq.heappush(p_queue, (color_val[c], m))

for elem in output:
    print(elem)
