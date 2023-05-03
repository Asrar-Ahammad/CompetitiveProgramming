def findDiffernce(nums1, nums2):
    answer = []
    nums = []
    for i in nums1:
        if i not in nums2:
            if i in nums:
                continue
            nums.append(i) 
    answer.append(nums)
    nums = []
    for i in nums2:
        if i not in nums1:
            if i in nums:
                continue
            nums.append(i)
    answer.append(nums)
    return answer

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(findDiffernce(nums1, nums2))