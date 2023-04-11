def reverse_sub_array(arr, N, k):
    # Solution 1
    # size = N
    # i = 0
    # sub_array_size = k-1
    # sub_array1 = []
    # sub_array2 = []

    # while i<k:
    #     sub_array1.append(arr[i])
    #     i+=1
    # sub_array1.reverse()
    # i = len(sub_array1)
    # while i < size:
    #     sub_array2.append(arr[i])
    #     i+=1
    # sub_array2.reverse()

    # arr = sub_array1 + sub_array2
    # result = ' '.join(map(str, arr))
    # return result

    # Solution 2
    for i in range(0,N,k):
        if i > N-k:
            arr[i:] = reversed(arr[i:])
        else:
            arr[i:i+k] = reversed(arr[i:i+k])
    return arr

arr = [1,2,3,4,5]
N = len(arr)
k = 4
print(reverse_sub_array(arr, N, k))
