test_case = int(input())
a = 0
while a < test_case:

    arr_size, geek_marks = input().split(' ')
    marks = [int(i) for i in input().split(' ')]
    arr_size = int(arr_size)
    geek_marks = int(geek_marks)
    j = 0
    count = 0
    while j < arr_size:
        if geek_marks < marks[j]:
            count += 1
        j += 1

    print(count)
    a += 1
