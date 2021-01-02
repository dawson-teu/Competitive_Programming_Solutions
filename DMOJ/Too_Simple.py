import string


def a():
    pass


def aaaaaaaaaaa():
    pass


def Hello():
    pass


def World():
    pass


b = string.punctuation[len(aaaaaaaaaaa.__name__)]
c = string.punctuation[len(a.__name__) - len(a.__name__)]

print(Hello.__name__ + b, World.__name__ + c)
