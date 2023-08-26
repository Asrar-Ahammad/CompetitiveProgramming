def numberPattern(n):
    i = 1
    j = 1
    arr = []
    a = []
    while i <= n:
        if len(a) == i:
            arr.append(a)
            a = []
            i += 1
        a.append(j)
        j += 1
        if j > 9:
            j = 1
    for b in arr:
        b.append(' '*(n-len(b)))
    for i in arr:
        for j in i:
            print(j,end=' ')
        print()
    print(arr)


numberPattern(15)