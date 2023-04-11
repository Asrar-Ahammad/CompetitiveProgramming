def binary_search(arr, k, n):
    low = 0
    high = n
    flag = 0
    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] == k:
            flag = 1
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    # if flag == 0:
    #     return -1


arr = [1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 21, 24, 26, 27, 31, 34, 46, 48]
n = len(arr)-1
k = 1
print(binary_search(arr, k, n))
print('n : ',n)
