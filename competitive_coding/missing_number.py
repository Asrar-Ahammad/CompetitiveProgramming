def missingNumber(A, N):
    prev = 0
    aft = 1
    A.sort()
    print(A)
    prev = A[0]
    count=0
    for i in A[1:]:
        if i-prev != 1:
            return i
        prev = i
        count+=1
    if N>count:
        return N

N = 4
A = [2, 1, 3]
print(missingNumber(A, N))
