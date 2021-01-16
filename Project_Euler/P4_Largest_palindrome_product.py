def isPalindrome(in_str):
    return in_str == in_str[::-1]


largest = -1
for i in range(100, 1000):
    for j in range(i, 1000):
        if isPalindrome(str(i * j)):
            largest = max(largest, i * j)
print(largest)
