def missing_number(nums):
    n = len(nums)
    return n*(n+1)//2 - sum(nums)


nums = [3, 0, 1] # Test case 1
nums = [9,6,4,2,3,5,7,0,1] # Test case 2
nums = [0,1] # Test case 3
print(missing_number(nums))
