def reverse_integer(x: int) -> int:
    x = str(x)
    if '-' in x:
        x = x[1:len(x)]
        x = x[::-1]
        x = int(x)
        x = str(x)
        x = '-'+x
    else:
        x = x[:len(x)]
        x = x[::-1]
        x = int(x)
        x = str(x)
    return int(x)


print(reverse_integer(120))
