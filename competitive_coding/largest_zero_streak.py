def largest_streak_of_zeros(x: str):
    if not x:
        return
    zero_max = []
    count = 0

    if x[-1] == '0':
        x = list(reversed(x))

    for char in x:
        if char == '0':
            count += 1
        else:
            zero_max.append(count)
        count = 0
        return max(zero_max) if zero_max else len(x)


s = input()
print(largest_streak_of_zeros(s))
