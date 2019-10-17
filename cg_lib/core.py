
def cross1(a):
    return -a[1], a[0]


def mul(a, b):
    return a[0] * b, a[1] * b


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def len2(a):
    return dot(a, a)


def dist2(a, b):
    return len2(sub(a, b))


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def area2(a, b, c):
    return cross(sub(b, a), sub(c, a))
