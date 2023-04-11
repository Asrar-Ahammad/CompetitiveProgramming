def remove_reverse(S):
    n = len(S)
    freq = {}
    for i in S:
        freq[i] = 0
    for i in S:
        if i in freq:
            freq[i]+=1
    start = 0
    end = n
    dir = 0 
    i = 0
    S = list(S)
    while start<=end:
        if dir == 0:
            if freq[S[i]] == 1:
                start+=1
            else:
                freq[S[i]]-=1
                S[i]='@'
                start +=1
                dir = 1
        else:
            if freq[S[i]] == 1:
                end-=1
            else:
                 freq[S[i]]-=1
                 S[i]='@'
                 end-=1
                 dir=0
    
    ans = ''
    for i in S:
        if i != '@':
            ans+=i

    return ans
S = "abab"
print(remove_reverse(S))