def rsa(nums):
    # result = []
    # for i in range(0, len(a)+1):
    #     result.append(sum(a[:i]))
    # return result[1:]
    for i in range(1,len(nums)):
        nums[i]+=nums[i-1]
    return nums


a = [1, 2, 3, 4]
print(rsa(a))
