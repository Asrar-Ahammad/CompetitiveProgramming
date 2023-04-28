def simplifyPath(s):
    ans = []
    for i in s:
        ans.append(i)

    i = 1
    while i < len(ans):
        if ans[i]=='/':
            if ans[i+1] == '/':
                ans.remove(ans[i])
        elif ans[i]=='.' :
            if ans[i+1] == '.':
                ans.remove(ans[i])
                ans.remove(ans[i+1])
        i+=1
    if len(ans)>1:
        if ans[-1]=='/':
            ans.pop()
    return "".join(ans)

path = "/home/"
print(simplifyPath(path))