def count_digits(n: int) -> int:
    count = 0
    for i in str(n):
        if int(i) == 0:
            continue
        if n % int(i) == 0:
            count += 1
    return count


print(count_digits(234))
