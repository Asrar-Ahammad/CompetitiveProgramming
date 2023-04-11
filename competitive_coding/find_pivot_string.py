# l = [1,2,3,4,5,6,7]
# print(l[4:])
# print(l[:3])

def pivotIndex(arr):
    for i in range(0, len(arr)):
        a1 = sum(arr[i + 1:])
        a2 = sum(arr[:i])
        if sum(arr[i + 1:]) == sum(arr[:i]):
            return i
    return -1


arr = [-1,-1,-1,1,1,1]
print(pivotIndex(arr))
