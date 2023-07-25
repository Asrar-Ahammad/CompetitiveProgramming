def mergeSortedArray(nums1, m, nums2, n):
    i = m-n
    j = 0
    while(i<m):
        nums1[i] = nums2[j]
        i+=1
        j+=1
    nums1 = sorted(nums1)
    print(nums1)
    # for i in range(m - n):
    #     print(nums1[i])

nums1 = [1,2,3,0,0,0]
m = len(nums1)
nums2 = [2,5,6]
n = len(nums2)
mergeSortedArray(nums1, m, nums2, n)
