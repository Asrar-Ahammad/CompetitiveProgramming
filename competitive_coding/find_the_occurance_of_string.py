def firstOccurance(haystack, needle):
    ans = []
    i = 0
    j = 0
    count = 0
    while i<len(haystack):
        if haystack[i]==needle[j]:
            ans.append(i)
            count+=1
            j+=1
            if count==len(needle):
                return ans[0]
        else:
            count=0
            i+=1
    return -1
haystack = "sadbutsad"
needle = "sad"

haystack = "leetcode"
needle = "leeto"
print(firstOccurance(haystack, needle))