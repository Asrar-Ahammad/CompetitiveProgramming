def lengthOfLastWord(s: str) -> int:
    i = len(s)-1
    count = 0
    while i>=0:
        if s[i] != " ":
            count+=1
        elif s[i] == " ":
            if count > 0:
                break
            else:
                i-=1
                continue
        i-=1
    return count

    # Second method
    # arr=s.split()
    # return len(arr[-1])
print(lengthOfLastWord('a'))