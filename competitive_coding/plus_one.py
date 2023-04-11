def plusOne(l):
    res = ''
    for i in l:
        res += str(i)
    res = int(res)
    res += 1
    l = []
    for i in str(res):
        l.append(int(i))
    return l


l = [9, 9]
print(plusOne(l))
