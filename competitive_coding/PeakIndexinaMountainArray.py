from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    # Linear search
    # max_index = 0
    # i = 0
    # if len(arr) < 3:
    #     return 0
    # while i < len(arr):
    #     if arr[i] > arr[max_index]:
    #         max_index = i
    #     i += 1
    # return max_index

    # Binary search
    r,l = len(arr)-1, 0
    while l<r:
        mid = (l+r-1)//2
        if arr[mid+1]<arr[mid] and arr[mid-1]<arr[mid]:
            return mid
        elif arr[mid+1]>arr[mid]:
            l = mid+1
        else:
            r = mid
    return mid
 


arr = [0, 1, 0]
arr = [0,10,5,2]
print(peakIndexInMountainArray(arr))
