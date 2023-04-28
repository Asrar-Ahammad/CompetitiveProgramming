def mergeSortedArray(nums1, m, nums2, n):
    for i in nums1:
        if nums1 == 0:
            nums1.pop(nums1.index(i))
    return nums1

nums1 = [1,2,3,4,0,0,0,0]
m = len(nums1)
nums2 = [2,5,6]
n = len(nums2)
print(mergeSortedArray(nums1,m,nums2,n))
