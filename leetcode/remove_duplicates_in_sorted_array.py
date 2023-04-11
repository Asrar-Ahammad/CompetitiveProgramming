def removeDuplicates(nums):
        # Two pointers
        i = 0 # unique pointer
        j = 1 # iterator pointer
        l = []
        while j < len(nums):
            a = nums[i]
            b = nums[j]
            if nums[i] != nums[j]:
                l.append(nums[i])
                nums[i] = nums[j]
            j += 1
        l.append(nums[i])
        return l[-2]

nums = [1,1,1,22,22,23]
# nums.reverse()
# print(nums)
print(removeDuplicates(nums))