def fibonacci(limit):
    fib_num = [1, 1]
    while fib_num[-1] + fib_num[-2] < limit:
        fib_num.append(fib_num[-1] + fib_num[-2])
    return fib_num


n = int(input())
sequence = input()

fibonacci_num = fibonacci(n)
valid = True
for i in range(n):
    if (i + 1) in fibonacci_num and not sequence[i] == 'A':
        valid = False
    elif not (i + 1) in fibonacci_num and sequence[i] == 'A':
        valid = False

if valid:
    print("That's quite the observation!")
else:
    print("Bruno, GO TO SLEEP")
