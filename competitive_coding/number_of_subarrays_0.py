def no_of_subarrays(n, arr):

    result = 0
    count = 0
    i = 0
    j = 0
    # O(n^2)
    # while i<n:
    #     j = i
    #     while j<n:
    #         if arr[j] == 0:
    #             count+=1
    #         else:
    #             break
    #         j+=1
    #     i+=1

    # O(n)
    while i<n:
        if arr[i] == 0:
            count+=1
        else:
            result += (count*(count+1)/2)
            count = 0
        i+=1
    if count > 0:
        result += (count*(count+1)/2)

    return result

arr = [1,3,0,0,2,0,0,4]
n = len(arr)
print(no_of_subarrays(n,arr))



