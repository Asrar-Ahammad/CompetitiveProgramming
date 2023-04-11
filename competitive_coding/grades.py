import math

n = int(input())
grades = []

for i in range(n):
    num = int(input())
    if num <= 37:
        num = num
    else:
        multiple = num/5
        multiple = math.trunc(multiple)
        difference = 5 * multiple
        sub = num - difference
        if sub < 0:
            sub = sub * -1
        if sub >= 3:
            num = num + (5 - sub)
    grades.append(num)

print(grades)
