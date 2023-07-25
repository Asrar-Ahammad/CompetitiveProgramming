from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    j = 1
    count = 0
    while (i < len(nums) and j < len(nums)):
        if nums[i] == nums[j]:
            count += 1
            if count >= 2:
                count -= 1
                nums.remove(nums[i])
                i-=1
                j-=1
            i += 1
            j += 1
        else:
            count = 0
            i += 1
            j += 1
    print(nums)


nums = [0,0,1,1,1,1,2,3,3]
removeDuplicates(nums)
