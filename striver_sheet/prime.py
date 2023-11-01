import math


def prime(n):
    count = 0
    if n % 2 == 0: return "No"

    for i in range(1, math.floor(math.sqrt(n+1))):
        if n % i == 0:
            count += 1

    if count > 2:
        return "No"
    else:
        return "Yes"


print(prime(9734523434523452))
