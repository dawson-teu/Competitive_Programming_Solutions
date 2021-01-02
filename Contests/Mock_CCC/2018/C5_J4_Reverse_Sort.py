def bubble_sort(arr):
    total = 0
    new_arr = arr[:]
    for i in range(len(new_arr)):
        sort_bool = False
        for j in range(len(new_arr) - 1):
            if new_arr[j + 1] > new_arr[j]:
                tmp = new_arr[j + 1]
                new_arr[j + 1] = new_arr[j]
                new_arr[j] = tmp
                sort_bool = True
                total += 1
        if not sort_bool:
            break
    return total


n = int(input())
line = input()
arr_in = [int(line.split(" ")[i]) for i in range(n)]

print(bubble_sort(arr_in))
