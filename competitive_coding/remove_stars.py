def removeStar(s):
    # Solution 1
    # l = []
    # for i in s:
    #     l.append(i)

    # i = 0
    # while i<len(l):
    #     if l[i]=='*':
    #         l.remove(l[i])
    #         l.remove(l[i-1])
    #         i=i-1
    #     else:
    #         i+=1
    # print(l)
    # q = ''
    # for i in l:
    #     q+=i
    # return q
    
    # Solution 2
    ans = []
    for i in s:
        if i == '*':
            ans.pop()
        else:
            ans.append(i)
    return "".join(ans)
s = "leet**cod*e"
s = "erase*****"
s = "il**autonrd**cl**nh*up*afpizp****d*a****lst" #"autonnlst"
# s = 'asde***asd*asdajd**'
print(removeStar(s))