import math


def areaSwitchCase(ch: int, a):
    # Write your code here
    pi = math.pi
    if ch == 1:
        return "{0:.5f}".format(pi * (a[0] * a[0]))
    elif ch == 2:
        return "{0:.5f}".format(a[0] * a[1])

print(areaSwitchCase(1,[12]))