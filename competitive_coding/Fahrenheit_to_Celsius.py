def ftc(s, e, w):
    i = 0
    while s <= e:
        i = (s - 32) * 5 / 9
        print(s, int(i))
        s += w


ftc(0, 100, 20)
