def partitionString(s):
    # Solution 1
    count = {}
    letters = set()
    i = 0
    sum = 0
    while i < len(s):
        if s[i] not in letters:
            letters.add(s[i])
            i+=1
        else:
            fset = frozenset(letters)
            if fset not in count:
                count[fset]=1
            else:
                    count[fset]+=1
            letters.clear()
    for i in count:
        sum = sum+count[i]

    return sum+1
            
    # Solution 2
    # count = 0
    # letters = ''
    # for i in s:
    #     if i in letters:
    #         count+=1
    #         letters = i
    #     else:
    #         letters+=i
    # return count+1


# s = "sssssss"
s = "abacaba"
print(partitionString(s))