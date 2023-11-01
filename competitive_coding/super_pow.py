def sup_pow(a, b):
    num = ''
    if a == 1:
        return 1
    else:
        for i in b:
            num += str(i)
        num = int(num)
        return a ** num


a = 2
b = [1, 0,3,5,6,7,2,3,4,6]

a = 1
b = [4, 3, 3, 8, 5, 2]

a = 2
b = [3,4,5,2,3,5,3,2]
print(sup_pow(a, b))
