def calculator_computation(x, y):
    result = x
    for num in range(y - 1):
        try:
            result = x ** result
        except OverflowError:
            return -1
    return result


def binary_search(minimum, maximum, computation):
    low = minimum
    high = maximum
    while high - low >= 10 ** (-5):
        middle = (low + high) / 2
        middle_func_val = calculator_computation(middle, computation[0])
        if middle_func_val < computation[1] and not middle_func_val == -1:
            low = middle
        else:
            high = middle
    return low


q = int(input())
queries = []
for i in range(q):
    queries.append([int(num) for num in input().split(" ")])

for query in queries:
    print(binary_search(1, 10, query))
