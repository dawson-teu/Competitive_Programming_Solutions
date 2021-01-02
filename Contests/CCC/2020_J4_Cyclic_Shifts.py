def is_cyclic(a, b):
    for x in range(len(b)):
        if a == b[x:] + b[:x]:
            return True
    return False


t = input()
s = input()
if len(s) > len(t):
    print("no")
elif len(s) == len(t):
    print("yes" if is_cyclic(s, t) else "no")
else:
    cyclic = False
    for i in range(len(t) - len(s) + 1):
        if is_cyclic(t[i:i + len(s)], s):
            cyclic = True
            break
    print("yes" if cyclic else "no")
