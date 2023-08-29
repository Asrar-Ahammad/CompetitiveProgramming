def sum_even_odd(n):
    n = str(n)
    even_sum = 0
    odd_sum = 0
    # for i in n:
    #     if int(i) % 2 == 0:
    #         even_sum += int(i)
    #     else:
    #         odd_sum += int(i)
    i = 0
    while i < len(n):
        if int(n[i]) % 2 == 0:
            even_sum += int(n[i])
        else:
            odd_sum += int(n[i])
        i += 1

    return even_sum, odd_sum


print(sum_even_odd(132456))
