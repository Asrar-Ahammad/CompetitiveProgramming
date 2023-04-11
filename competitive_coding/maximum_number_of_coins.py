def max_number_of_coins(arr, N):

    size = N-1
    count = 0
    i = 1
    result = 0

    while True:
        if size >=3:
            result = arr[i-1]*arr[i]*arr[i+1]
            arr.pop(i)
            size = len(arr)
        elif size<3:
            i = 0
            result = arr[i]+arr[i+1]
            arr.pop(i)
        elif size == 0:
            break
    return result

