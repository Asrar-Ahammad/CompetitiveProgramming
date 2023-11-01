def reverse_integer(x):
    rev_num = 0
    while (x > 0):
        ld = x % 10
        rev_num = int((rev_num * 10) + ld)
        x = x // 10
    return rev_num


print(reverse_integer(-1234))
