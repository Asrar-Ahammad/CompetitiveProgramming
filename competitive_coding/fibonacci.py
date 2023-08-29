def fibonacci(num):
    a = 1
    b = 1
    c = 0
    if num == 1 or num == 2:
        return 1
    else:
        for i in range(2, num):
            c = a + b
            a = b
            b = c
        return c


n = int(input("Enter number : "))
print(fibonacci(n))
