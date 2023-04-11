def firstElementsKtimes(A, N, K):
    count = {}
    l = []
    for i in A:
        count[i]=0
    for i in A:
        count[i] = count[i]+1
        if count[i] == K:
            l.append(i)
            break
        if l == []:
            l.append(-1)
    return min(l)
A = [5,4,3,4]
N = 4
K = 3

print(firstElementsKtimes(A, N, K))