def searchInsert(nums, target):
    if target > max(nums):
        return len(nums)
    if target < min(nums):
        return 0
    if target in nums:
        return nums.index(target)
    low = 0
    high = len(nums)
    mid = 0
    while low < high:
        mid = (high+low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if nums[mid-1]<target:
                return mid
            else:
                high = mid-1
        else:
            if nums[mid+1]>target:
                return mid+1
            else:
                low = mid+1

nums = [1,3,5,6]
target = 2
nums =[1,3]
target = 1
print(searchInsert(nums, target))
