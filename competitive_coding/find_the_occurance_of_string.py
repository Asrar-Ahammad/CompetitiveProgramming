def firstOccurance(haystack, needle):
    # Approach 1
    # ans = []
    # i = 0
    # j = 0
    # count = 0
    # while i<len(haystack):
    #     if haystack[i]==needle[j]:
    #         ans.append(i)
    #         count+=1
    #         j+=1
    #         if count==len(needle):
    #             return ans[0]
    #     else:
    #         count=0
    #         i+=1
    # return -1

    # Approach 2
    # count = 0
    # j = 0
    # index = 0
    # i = 0
    # while i < len(haystack):
    #     if haystack[i] == needle[j]:
    #         count +=1
    #         j+=1
    #         index = i-(len(needle)-1)
    #     elif haystack[i] != needle[j]:
    #         count = 0
    #         j = 0
    #     if count == len(needle):
    #         return index
    #     i+=1
    # return -1

    # Solution 
    m = len(needle)
    n = len(haystack)

    for window_start in range(n - m + 1):
        for i in range(m):
            if needle[i] != haystack[window_start + i]:
                break
            if i == m - 1:
                return window_start

        return -1
haystack = "sadbutsad"
needle = "sad"

# haystack = "leetcode"
# needle = "leeto"

haystack = "mississippi"
needle = "issip"
print(firstOccurance(haystack, needle))