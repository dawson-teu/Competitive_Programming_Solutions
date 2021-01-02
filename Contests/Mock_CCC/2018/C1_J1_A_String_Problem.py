def no_zero(val):
    for digit in str(val):
        if digit == "0":
            return False
    return True


n = int(input())
for i in range(n + 1, 1111112):
    if no_zero(i):
        print(i)
        break
