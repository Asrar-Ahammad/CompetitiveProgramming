def sum_of_divisors(n):
    # O(n²) time complexity
    sum = 0
    i = 1
    # while i <= n:
    #     j = 1
    #     while j <= i:
    #         if i % j == 0:
    #             sum += j
    #         j += 1
    #     i += 1

    while i <= n:
        j = 1
        while j <= (i ** (1 / 2)):
            if i / j == 0 and i / j != j:
                sum += j
            j += 1
        i += 1
    return sum


print(sum_of_divisors(10))
