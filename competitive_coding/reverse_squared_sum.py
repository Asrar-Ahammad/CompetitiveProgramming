T = int(input('Enter number of test cases :'))
i = 0
while i < T:
    i += 1
    N = int(input('Enter size of Array :'))
    print('Enter array elements')
    array = list(map(int, input().split()))

    j = N - 1
    result = array[j] * array[j]
    count = 1
    while j != 0:
        count += 1
        j -= 1
        if count % 2 == 0:
            result -= (array[j] * array[j])
        else:
            result += (array[j] * array[j])
    print('result : ', result)
