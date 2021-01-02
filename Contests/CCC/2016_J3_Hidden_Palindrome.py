def is_palindrome(s):
    return s[::-1] == s


string = input()
max_len = -1
for i in range(len(string) + 1):
    for j in range(i + 1, len(string) + 1):
        if is_palindrome(string[i:j]):
            max_len = max(max_len, len(string[i:j]))
print(max_len)
