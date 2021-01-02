def is_prime(n):
    if n < 2:
        return "not"
    for i in range(2, n):
        if n % i == 0:
            return "not"
    return "prime"


print(is_prime(int(input())))
