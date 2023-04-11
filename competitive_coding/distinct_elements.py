def countDistinct(A, N):
    left = []
    right = []
    s = set()
    
    i = 0
    while i < N:
        left.append(len(s))
        s.add(A[i])
        i+=1
    s.clear()

    i = N-1
    while i >= 0:
        right.append(len(s))
        s.add(A[i])
        i-=1

    i = 0
    ans = []
    right.reverse()
    while i<N:
        ans.append(left[i]-right[i])
        i+=1
    
    return ans

arr = [4,3,3]
N = 3
print(countDistinct(arr, N))